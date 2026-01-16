# Learning Objective:
# This tutorial will teach you how to visualize a simple dataset and
# tell a basic story about its trends using the Matplotlib library in Python.
# We will focus on creating a line plot to show how a value changes over time.

# Import the necessary library for plotting
# Matplotlib is the go-to library for creating static, animated, and interactive visualizations in Python.
# We import it as 'plt' for brevity, a common convention.
import matplotlib.pyplot as plt

# --- Section 1: Preparing Our Data ---

# Let's create some sample data to work with.
# For this tutorial, we'll imagine we're tracking the number of users
# visiting a website over a few days.

# 'days' will represent our x-axis values (e.g., days of the week or month).
# This is a list of integers representing the sequential order of days.
days = [1, 2, 3, 4, 5, 6, 7]

# 'users' will represent our y-axis values (e.g., number of users).
# This is a list of integers representing the corresponding user count for each day.
users = [150, 165, 180, 175, 190, 205, 220]

# --- Section 2: Creating the Plot ---

# Now, let's use Matplotlib to visualize this data.

# plt.figure(figsize=(10, 6))
# This line creates a new figure (a window or canvas for your plot).
# 'figsize' sets the width and height of the figure in inches.
# A larger size can make the plot easier to read.
# For this simple example, we can often skip this and let Matplotlib
# decide the default size, but it's good practice to know about it.
plt.figure(figsize=(10, 6))

# plt.plot(days, users)
# This is the core function for creating a line plot.
# It takes two arguments:
# 1. The data for the x-axis (our 'days' list).
# 2. The data for the y-axis (our 'users' list).
# Matplotlib automatically connects the points with lines.
plt.plot(days, users)

# --- Section 3: Enhancing the Plot (Telling the Story) ---

# To make our plot understandable and tell a story, we need labels and a title.

# plt.title("Website User Growth Over a Week")
# 'title()' adds a descriptive title to our plot, explaining what it represents.
# This is crucial for context.
plt.title("Website User Growth Over a Week")

# plt.xlabel("Day of the Week")
# 'xlabel()' adds a label to the x-axis, clarifying what the x-axis represents.
plt.xlabel("Day of the Week")

# plt.ylabel("Number of Users")
# 'ylabel()' adds a label to the y-axis, clarifying what the y-axis represents.
plt.ylabel("Number of Users")

# plt.grid(True)
# 'grid(True)' adds a grid to the plot.
# This makes it easier to read specific values by aligning them with the axes.
plt.grid(True)

# --- Section 4: Adding a Simple Trend Interpretation (The Story) ---

# We can add annotations to highlight specific points or trends.

# Let's find the day with the most users and the day with the fewest users.
# 'max(users)' finds the highest user count.
# 'users.index(max(users))' finds the index (position) of that highest count.
# We add 1 to the index because our 'days' list starts from 1, not 0.
peak_day_index = users.index(max(users))
peak_day = days[peak_day_index]
peak_users = max(users)

# Similarly for the minimum.
min_day_index = users.index(min(users))
min_day = days[min_day_index]
min_users = min(users)

# plt.annotate() is a powerful function to add text at specific points on the plot.
# It's great for highlighting key findings.

# Annotate the peak day:
# We tell Matplotlib to place text at the coordinates (peak_day, peak_users).
# 'text' is the string to display.
# 'xytext' is where the text label itself will be positioned, often slightly offset
# from the point it's annotating. We use a small offset here.
# 'arrowprops' defines the style of the arrow pointing from the text to the annotated point.
plt.annotate(f'Peak: {peak_users} users',
             xy=(peak_day, peak_users),
             xytext=(peak_day + 0.5, peak_users + 10), # Position text slightly above and to the right
             arrowprops=dict(facecolor='black', shrink=0.05)) # Arrow style

# Annotate the minimum day:
plt.annotate(f'Low: {min_users} users',
             xy=(min_day, min_users),
             xytext=(min_day + 0.5, min_users - 20), # Position text slightly below and to the right
             arrowprops=dict(facecolor='black', shrink=0.05)) # Arrow style

# --- Section 5: Displaying the Plot ---

# plt.show()
# This command actually displays the plot that we've built.
# Without this, the plot would be created in memory but not shown on your screen.
plt.show()

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Matplotlib installed: pip install matplotlib
# 2. Save this code as a Python file (e.g., plot_story.py).
# 3. Run it from your terminal: python plot_story.py

# You will see a window pop up displaying the line graph.
# The graph will show the user growth trend.
# The title and axis labels will explain the data.
# The annotations will highlight the day with the most and fewest users.
# This visual representation helps us quickly understand that website traffic
# has generally increased over the week, with a dip on day 4, reaching its
# highest point on day 7.

# The "story" here is simple: website users are growing, but there was a small fluctuation.
# We can interpret this by looking at the shape of the line and the annotated points.