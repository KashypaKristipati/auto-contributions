# Learning Objective:
# This tutorial will guide you through building a basic real-time chatbot in Python
# that analyzes user sentiment using a cloud-based Natural Language Processing (NLP) API.
# We will focus on understanding how to:
# 1. Interact with a cloud NLP API to send text and receive analysis.
# 2. Process the API's response to extract sentiment.
# 3. Implement a simple loop for real-time chat interaction.
#
# For this tutorial, we will use the Google Cloud Natural Language API.
# You will need to set up a Google Cloud project and enable the Natural Language API.
# Instructions for setting up Google Cloud and obtaining credentials can be found here:
# https://cloud.google.com/natural-language/docs/setup
#
# **IMPORTANT**: Replace 'YOUR_GOOGLE_CLOUD_PROJECT_ID' with your actual project ID.
# You'll also need to set up your GOOGLE_APPLICATION_CREDENTIALS environment variable.

# Import necessary libraries
# google.cloud.language allows us to interact with the Google Cloud Natural Language API
from google.cloud import language_v1
# os is used to access environment variables, which is a secure way to handle credentials
import os

# --- Configuration ---
# Set the Google Cloud project ID. This is where your NLP API calls will be billed.
# It's good practice to avoid hardcoding sensitive information directly in the code.
# In a real-world application, you might use configuration files or more robust
# environment variable management.
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT_ID", "YOUR_GOOGLE_CLOUD_PROJECT_ID") # Replace or set env var

# --- Sentiment Analysis Function ---
def analyze_sentiment(text_content: str) -> dict:
    """
    Analyzes the sentiment of the given text content using Google Cloud Natural Language API.

    Args:
        text_content (str): The text string to analyze.

    Returns:
        dict: A dictionary containing the sentiment score and magnitude.
              Returns None if an error occurs or no sentiment is found.
    """
    # Instantiate a client for the Natural Language API.
    # This client will handle the communication with Google Cloud.
    client = language_v1.LanguageServiceClient()

    # Construct the document object. The API needs to know what text it's analyzing.
    # We specify the encoding type as UTF-8, which is standard for most text.
    document = language_v1.Document(
        content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Call the analyze_sentiment method on the client.
    # This is the core operation that sends our text to Google Cloud for analysis.
    try:
        response = client.analyze_sentiment(request={"document": document})
    except Exception as e:
        print(f"Error calling Google Cloud NLP API: {e}")
        return None

    # Process the response from the API.
    # The response object contains detailed information about the sentiment.
    # We are primarily interested in the overall sentiment of the document.
    sentiment = response.document_sentiment

    # The sentiment score ranges from -1.0 (negative) to 1.0 (positive).
    # The magnitude indicates the overall strength of emotion (both positive and negative)
    # within the text. A higher magnitude means stronger emotion.

    # Return a dictionary containing the sentiment score and magnitude.
    return {
        "score": sentiment.score,
        "magnitude": sentiment.magnitude
    }

# --- Chatbot Logic ---
def run_chatbot():
    """
    Runs a simple real-time chatbot that prompts the user for input and
    analyzes the sentiment of their messages.
    """
    print("Welcome to the Sentiment Chatbot!")
    print("Type 'quit' to exit.")
    print("------------------------------------")

    # Start an infinite loop to keep the chatbot running until the user quits.
    while True:
        # Prompt the user for input.
        user_input = input("You: ")

        # Check if the user wants to quit.
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break # Exit the loop

        # Analyze the sentiment of the user's input.
        sentiment_result = analyze_sentiment(user_input)

        # Display the sentiment analysis results.
        if sentiment_result:
            score = sentiment_result["score"]
            magnitude = sentiment_result["magnitude"]

            # Provide feedback based on the sentiment score.
            if score >= 0.5:
                sentiment_label = "Positive"
            elif score <= -0.5:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"

            print(f"Chatbot: Your message sentiment is: {sentiment_label} (Score: {score:.2f}, Magnitude: {magnitude:.2f})")
        else:
            # If sentiment analysis failed, inform the user.
            print("Chatbot: Sorry, I couldn't analyze your sentiment.")

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that run_chatbot() is called only when the script
    # is executed directly (not when imported as a module).
    # This is a standard Python best practice.
    run_chatbot()

# Example interactions (after running the script and typing "quit"):
#
# Welcome to the Sentiment Chatbot!
# Type 'quit' to exit.
# ------------------------------------
# You: I love this tutorial, it's so helpful!
# Chatbot: Your message sentiment is: Positive (Score: 0.90, Magnitude: 1.80)
# You: This is a bit confusing.
# Chatbot: Your message sentiment is: Negative (Score: -0.70, Magnitude: 1.40)
# You: The weather is okay today.
# Chatbot: Your message sentiment is: Neutral (Score: 0.10, Magnitude: 0.20)
# You: quit
# Chatbot: Goodbye!