# Learning Objective: Visualize your CSV data to tell compelling stories with charts and graphs.
# This tutorial will guide you through reading a CSV file, performing basic data manipulation,
# and creating a simple but informative line chart using the 'pandas' and 'matplotlib' libraries in Python.
# We will focus on understanding how to represent trends over time or across categories.

# --- Part 1: Importing Necessary Libraries ---

# We need pandas to read and manipulate our data, and matplotlib.pyplot to create plots.
# These are standard libraries for data analysis and visualization in Python.
import pandas as pd
import matplotlib.pyplot as plt

# --- Part 2: Preparing Example Data (or Reading a CSV) ---

# For this tutorial, we'll create a sample DataFrame directly.
# In a real-world scenario, you would typically read your data from a CSV file
# using: df = pd.read_csv('your_data.csv')

# Let's create some sample data that represents monthly sales over a few years.
# This kind of data is perfect for showing trends.
data = {
    'Month': pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01',
                             '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01',
                             '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01',
                             '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']),
    'Sales': [100, 110, 120, 130, 125, 140, 150, 145, 160, 170, 180, 190,
              185, 195, 205, 215, 210, 220, 230, 225, 240, 250, 260, 270]
}

# Create a pandas DataFrame from our sample data.
# A DataFrame is like a table, very useful for organizing data.
df = pd.DataFrame(data)

# It's good practice to inspect the first few rows of your DataFrame to ensure it loaded correctly.
print("Sample DataFrame Head:")
print(df.head())
print("\n") # Print a newline for better readability

# --- Part 3: Creating a Line Chart to Show Trends ---

# We want to visualize the 'Sales' trend over 'Month'. A line chart is ideal for this.
# The x-axis will represent time (Month), and the y-axis will represent the quantity (Sales).

# Create a figure and an axes object. This is the canvas and the plot area.
fig, ax = plt.subplots(figsize=(12, 6)) # figsize sets the width and height of the plot in inches.

# Plot the data: 'Month' on the x-axis, 'Sales' on the y-axis.
# The 'marker' argument adds points to the line, making individual data points visible.
ax.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='skyblue')

# --- Part 4: Enhancing the Chart for Storytelling ---

# Good charts need labels and a title to be understood easily.
# These elements help tell the "story" of the data.

# Set the title of the plot. This should be descriptive.
ax.set_title('Monthly Sales Trend (2022-2023)', fontsize=16)

# Label the x-axis.
ax.set_xlabel('Date', fontsize=12)

# Label the y-axis.
ax.set_ylabel('Sales Revenue ($)', fontsize=12)

# Add a grid to make it easier to read values.
ax.grid(True, linestyle='--', alpha=0.6) # alpha controls transparency

# Improve date formatting on the x-axis for better readability.
# This automatically handles how dates are displayed.
fig.autofmt_xdate()

# Add a legend. Even with one line, it's good practice.
# It helps identify what each line represents.
ax.legend(['Sales'])

# --- Part 5: Displaying the Chart ---

# This command renders the plot. Without it, the plot won't appear.
plt.tight_layout() # Adjusts plot to prevent labels overlapping.
plt.show()

# --- Example Usage ---
# To use this with your own CSV file:
# 1. Save your CSV file (e.g., 'my_sales_data.csv') in the same directory as your Python script.
# 2. Make sure your CSV has at least two columns: one for the x-axis (e.g., 'Date' or 'Month')
#    and one for the y-axis (e.g., 'Revenue' or 'Quantity').
# 3. Replace the DataFrame creation part with:
#    df = pd.read_csv('my_sales_data.csv')
# 4. Ensure the column names used in df['Month'] and df['Sales'] match your CSV file.
#    For dates, pandas might need help parsing them correctly. You might need:
#    df['YourDateColumn'] = pd.to_datetime(df['YourDateColumn'])
# 5. Adjust the plot labels and title to reflect your data.

# For instance, if your CSV has columns 'OrderDate' and 'TotalAmount':
# df = pd.read_csv('your_orders.csv')
# df['OrderDate'] = pd.to_datetime(df['OrderDate']) # Convert to datetime objects
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(df['OrderDate'], df['TotalAmount'], marker='.', color='coral')
# ax.set_title('Order Amount Over Time', fontsize=14)
# ax.set_xlabel('Order Date', fontsize=11)
# ax.set_ylabel('Total Amount ($)', fontsize=11)
# ax.grid(True, linestyle=':', alpha=0.5)
# fig.autofmt_xdate()
# ax.legend(['Total Order Amount'])
# plt.tight_layout()
# plt.show()