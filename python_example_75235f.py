# Learn to create interactive data visualizations using Python and Plotly

# This tutorial will guide you through the process of creating your first
# interactive data visualization using the Plotly Python library.
# We will focus on creating a simple scatter plot that allows users to
# hover over data points to see their specific values.

# Plotly is a powerful library for creating interactive, publication-quality
# graphs online. It's excellent for data exploration and sharing insights.
# We'll use Plotly Express, a high-level API that makes it easy to create
# common plot types with minimal code.

# --- Installation ---
# If you don't have Plotly installed, you can install it using pip:
# pip install plotly pandas

# --- Importing Libraries ---
# We need 'plotly.express' for creating the plots and 'pandas' for
# handling our data. Pandas DataFrames are a very common and convenient
# way to structure data for plotting.
import plotly.express as px
import pandas as pd

# --- Creating Sample Data ---
# For demonstration purposes, let's create a small, simple dataset.
# In a real-world scenario, you would load your data from a CSV,
# database, or API.
# We'll create a dictionary where keys are column names and values
# are lists of data.
data = {
    'X_Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y_Value': [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Size': [20, 30, 25, 35, 28, 22, 33, 27, 21, 31]
}

# Convert the dictionary into a pandas DataFrame.
# DataFrames are tabular data structures that are easy to manipulate and
# analyze. Plotly works very well with DataFrames.
df = pd.DataFrame(data)

# --- Creating the Interactive Scatter Plot ---
# We'll use `plotly.express.scatter()` to create our scatter plot.
# This function takes the DataFrame and mappings for x, y, color, and size.

# `df`: The pandas DataFrame containing our data.
# `x='X_Value'`: Specifies which column from the DataFrame to use for the x-axis.
# `y='Y_Value'`: Specifies which column to use for the y-axis.
# `color='Category'`: This is where the interactivity really starts!
#                     Plotly will automatically assign different colors
#                     to points based on their 'Category' value.
#                     This also adds a legend that allows users to
#                     filter points by category by clicking on legend items.
# `size='Size'`: This maps the 'Size' column to the size of the markers.
#                Larger values in the 'Size' column will result in larger dots.
# `hover_name='Category'`: When you hover over a point, the 'Category'
#                          value will be prominently displayed.
# `hover_data=['X_Value', 'Y_Value', 'Size']`: Specifies additional data
#                                              columns to show in the
#                                              hover tooltip.
# `title='Interactive Scatter Plot Example'`: Sets a title for our plot.
fig = px.scatter(df,
                 x='X_Value',
                 y='Y_Value',
                 color='Category',
                 size='Size',
                 hover_name='Category',
                 hover_data=['X_Value', 'Y_Value', 'Size'],
                 title='Interactive Scatter Plot Example')

# --- Displaying the Plot ---
# The `fig.show()` method renders the plot.
# In an interactive environment like a Jupyter Notebook or Google Colab,
# this will display the plot directly. If you run this as a script,
# it will typically open the plot in your default web browser.
# This generated plot is HTML-based, making it highly portable and
# interactive.
fig.show()

# --- What makes this interactive? ---
# 1. Hovering: Moving your mouse over a data point displays detailed information.
# 2. Zooming/Panning: You can use your mouse wheel to zoom and click-and-drag to pan.
# 3. Legend Interaction: Clicking on items in the legend (e.g., 'A', 'B', 'C')
#    will toggle the visibility of points belonging to that category.
# 4. Tool Bar: Plotly provides a toolbar on hover with options like saving
#    the plot as an image.

# This is a basic example, but Plotly can create many other plot types
# (line charts, bar charts, heatmaps, etc.) with similar interactive features.
# The key is understanding how to map your data columns to visual properties
# like position (x, y), color, size, and shape.

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Python, pandas, and plotly installed.
# 2. Save the code as a .py file (e.g., 'interactive_plot.py').
# 3. Run it from your terminal: 'python interactive_plot.py'
#    or execute it in a Jupyter Notebook/Colab cell.