# Learning Objective:
# This tutorial teaches how to implement an asynchronous Python program
# to concurrently fetch data from multiple URLs using the `asyncio` library
# for concurrency and the `aiohttp` library for making HTTP requests.
# You will learn about `async def`, `await`, `asyncio.gather`, and
# efficient HTTP client session management.

import asyncio
import aiohttp
import time
import logging

# Configure basic logging for better output during execution.
# This helps us see when each fetch starts and finishes.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. Define an asynchronous function to fetch a single URL
async def fetch_url(session: aiohttp.ClientSession, url: str) -> tuple[str, str]:
    """
    Fetches the content of a single URL asynchronously.

    Args:
        session: An aiohttp.ClientSession instance, reused for efficiency.
                 Reusing the session pools connections and avoids overhead
                 like repeated TLS handshakes.
        url: The URL to fetch.

    Returns:
        A tuple containing the URL and its fetched text content (or an error message).
    """
    logging.info(f"Starting fetch for: {url}")
    try:
        # 'async with' ensures resources (like network connections) are properly
        # released, even if errors occur.
        # 'await' pauses the execution of *this specific coroutine* until the
        # HTTP request completes. However, crucially, it allows the asyncio
        # event loop to switch to and run *other* coroutines/tasks in the meantime.
        async with session.get(url) as response:
            # Raise an exception for HTTP errors (4xx or 5xx responses).
            response.raise_for_status()
            # Await the reading of the response body as text.
            # This is another I/O operation (reading from the network stream)
            # that can be awaited, allowing further concurrency.
            text_content = await response.text()
            logging.info(f"Finished fetch for: {url} (Status: {response.status})")
            # We'll return just a snippet to keep the output manageable
            return url, text_content[:100] + "..."
    except aiohttp.ClientError as e:
        # Catch aiohttp-specific errors, which include network issues,
        # DNS failures, and HTTP status errors (from raise_for_status).
        logging.error(f"Error fetching {url}: {e}")
        return url, f"Error: {type(e).__name__} - {e}"
    except Exception as e:
        # Catch any other unexpected errors that might occur.
        logging.error(f"An unexpected error occurred for {url}: {e}")
        return url, f"Unexpected Error: {type(e).__name__} - {e}"

# 2. Define the main asynchronous function to fetch multiple URLs concurrently
async def fetch_all_urls(urls: list[str]) -> list[tuple[str, str]]:
    """
    Fetches data from a list of URLs concurrently using asyncio and aiohttp.

    Args:
        urls: A list of URLs to fetch.

    Returns:
        A list of tuples, where each tuple contains (url, fetched_data_or_error).
        The order of results corresponds to the order of input URLs.
    """
    logging.info(f"Starting concurrent fetching of {len(urls)} URLs.")
    # Create a single aiohttp.ClientSession instance for all requests.
    # This is a best practice for `aiohttp`. It's crucial for performance
    # as it manages a connection pool, reducing the overhead of establishing
    # new connections for each request.
    # 'async with' ensures the session is properly closed when all fetches are done.
    async with aiohttp.ClientSession() as session:
        # Create a list of 'tasks' (actually, coroutine objects in this case).
        # Each call to `fetch_url(session, url)` returns a coroutine object
        # that describes an asynchronous operation. These are not yet running.
        tasks = [fetch_url(session, url) for url in urls]

        # `asyncio.gather()` takes multiple awaitables (our coroutines/tasks)
        # and efficiently runs them concurrently. It waits for all of them
        # to complete and collects their results in a list.
        # The `*tasks` syntax unpacks our list of coroutines into separate
        # arguments for `asyncio.gather()`.
        results = await asyncio.gather(*tasks)
    logging.info("All URL fetches completed.")
    return results

# 3. Example Usage: How to run your asynchronous program
if __name__ == "__main__":
    # Define a list of URLs to fetch.
    # We include a 'delay' URL from httpbin.org to simulate a slow server response.
    # This URL will intentionally take 3 seconds to respond, vividly highlighting
    # the benefit of concurrency (total time will be closer to 3s than sum of all delays).
    example_urls = [
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://httpbin.org/delay/3", # This URL will take ~3 seconds to respond
        "https://www.python.org",
        "https://www.example.com",
        "https://bad-url-does-not-exist.com" # Example of a URL that will intentionally fail
    ]

    print("--- Starting Asynchronous URL Fetching ---")
    start_time = time.perf_counter() # Record the start time to measure total execution.

    # asyncio.run() is the main entry point for running the top-level
    # asynchronous function (our `fetch_all_urls` coroutine).
    # It sets up and manages the asyncio event loop, allowing our
    # `async` functions to execute.
    fetched_data = asyncio.run(fetch_all_urls(example_urls))

    end_time = time.perf_counter() # Record the end time.
    duration = end_time - start_time

    print("\n--- Fetching Results ---")
    for url, data in fetched_data:
        print(f"URL: {url}")
        print(f"Data: {data}\n") # Print the snippet or error message

    print(f"--- Total time taken: {duration:.2f} seconds ---")
    print("\nNote: Even with a URL specifically designed to take 3 seconds, the total time")
    print("for all fetches is close to 3 seconds, not the sum of individual fetch times.")
    print("This demonstrates that the fetches ran concurrently, leveraging `asyncio`'s")
    print("ability to switch between I/O-bound tasks while waiting.")