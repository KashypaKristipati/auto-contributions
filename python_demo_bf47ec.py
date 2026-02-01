# Learning Objective:
# This script demonstrates how to generate a simple narrative from structured data
# using text generation and visualize key insights from that data using basic plotting.
# It's designed for beginners to understand how code can transform raw information into
# a story and visual representation.

# Import necessary libraries
import pandas as pd  # pandas is great for handling structured data (like tables)
from faker import Faker  # faker is a library to generate fake data, useful for examples
import matplotlib.pyplot as plt  # matplotlib is a powerful plotting library for visualizations
import random  # random is useful for making choices, like selecting narrative elements

# Initialize the Faker object for generating realistic-looking fake data
fake = Faker()

# --- Data Generation (for demonstration purposes) ---
# In a real-world scenario, you'd load your data from a file (CSV, Excel, etc.)
def generate_sample_data(num_records=10):
    """
    Generates a sample pandas DataFrame representing product sales data.
    This helps us have data to work with without needing an external file.
    """
    data = []
    for _ in range(num_records):
        # Create a record with fake product names, categories, sales figures, and ratings
        product_name = fake.catch_phrase()  # e.g., "Intelligent Eco-Friendly Keyboard"
        category = random.choice(['Electronics', 'Apparel', 'Home Goods', 'Books'])
        sales = random.randint(50, 1000)  # Simulate sales figures
        rating = round(random.uniform(3.0, 5.0), 1) # Simulate star ratings
        data.append({
            'Product Name': product_name,
            'Category': category,
            'Sales': sales,
            'Rating': rating
        })
    return pd.DataFrame(data) # Convert the list of dictionaries into a pandas DataFrame

# --- Text Generation ---
def generate_product_narrative(dataframe):
    """
    Generates a short narrative about the products in the DataFrame.
    This function focuses on extracting key information and weaving it into sentences.
    """
    narrative = "Here's a brief overview of our product performance:\n\n"

    # Find the product with the highest sales
    top_seller = dataframe.loc[dataframe['Sales'].idxmax()]
    narrative += f"The top-selling product is '{top_seller['Product Name']}' from the {top_seller['Category']} category, with an impressive {top_seller['Sales']} units sold. "

    # Find the product with the highest rating
    top_rated = dataframe.loc[dataframe['Rating'].idxmax()]
    narrative += f"In terms of customer satisfaction, '{top_rated['Product Name']}' stands out with a rating of {top_rated['Rating']} stars. "

    # Count products by category to understand distribution
    category_counts = dataframe['Category'].value_counts()
    narrative += "Our product distribution across categories shows that "
    for category, count in category_counts.items():
        narrative += f"we have {count} products in {category}, "
    narrative = narrative.rstrip(', ') + ".\n" # Clean up the trailing comma and space

    # Add a general concluding remark
    narrative += "Overall, the data suggests a healthy and diverse product line."

    return narrative

# --- Data Visualization ---
def visualize_sales_by_category(dataframe):
    """
    Creates a bar chart visualizing the total sales for each product category.
    This helps us see which categories are performing best in terms of revenue.
    """
    # Group data by category and sum the sales for each category
    sales_by_category = dataframe.groupby('Category')['Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6)) # Set the size of the plot for better readability
    sales_by_category.plot(kind='bar', color='skyblue') # Create a bar chart
    plt.title('Total Sales by Product Category') # Set the title of the chart
    plt.xlabel('Category') # Label the x-axis
    plt.ylabel('Total Sales') # Label the y-axis
    plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better visibility
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.show() # Display the plot

# --- Main Execution Block ---
if __name__ == "__main__":
    # This block runs only when the script is executed directly (not imported as a module)

    # 1. Generate sample data
    print("Generating sample data...")
    product_data = generate_sample_data(num_records=15) # Create 15 sample product records
    print("Sample data generated:\n", product_data.head()) # Display the first few rows of the generated data
    print("-" * 30) # Separator for clarity

    # 2. Generate narrative from the data
    print("Generating narrative...")
    story = generate_product_narrative(product_data)
    print(story)
    print("-" * 30) # Separator for clarity

    # 3. Visualize key insights from the data
    print("Generating visualization...")
    visualize_sales_by_category(product_data)
    print("Visualization complete. Check the displayed plot.")

# --- Example Usage ---
# To run this script:
# 1. Save it as a Python file (e.g., narrative_generator.py).
# 2. Make sure you have pandas, faker, and matplotlib installed:
#    pip install pandas faker matplotlib
# 3. Run it from your terminal:
#    python narrative_generator.py
#
# The script will:
# - Create sample product data.
# - Print a narrative summarizing the data.
# - Display a bar chart of sales per category.