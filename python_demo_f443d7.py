# Fractal Generation with Recursion and Matplotlib in Python

# Learning Objective:
# This tutorial demonstrates how to programmatically generate intricate fractal art
# using the power of recursion and basic plotting with the Matplotlib library in Python.
# We will focus on understanding the concept of self-similarity and how recursive
# functions can be used to create complex patterns from simple rules.

# Import necessary libraries.
# Matplotlib is a plotting library that will allow us to visualize our fractal.
# The 'pyplot' module provides a MATLAB-like interface for creating plots.
import matplotlib.pyplot as plt

# --- Fractal Generation Function ---

# Define a recursive function to draw a fractal.
# Fractals are characterized by self-similarity: a part of the fractal
# resembles the whole, at different scales. Recursion is a natural way
# to model this behavior.
def draw_fractal(ax, x, y, length, angle, depth):
    """
    Recursively draws a fractal pattern.

    Args:
        ax (matplotlib.axes.Axes): The axes object to draw on.
        x (float): The starting x-coordinate of the current line segment.
        y (float): The starting y-coordinate of the current line segment.
        length (float): The length of the current line segment.
        angle (float): The angle (in degrees) of the current line segment
                       relative to the positive x-axis.
        depth (int): The current recursion depth. This controls how many
                     times the pattern is repeated.
    """
    # Base case: If the depth reaches 0, we stop recursing.
    # This is crucial to prevent infinite recursion and to define the
    # smallest elements of our fractal.
    if depth == 0:
        return

    # Calculate the endpoint of the current line segment.
    # We use trigonometry (sine and cosine) to determine the x and y
    # displacement based on length and angle. The angle needs to be
    # converted to radians for Python's math functions.
    import math
    rad_angle = math.radians(angle)
    x_end = x + length * math.cos(rad_angle)
    y_end = y + length * math.sin(rad_angle)

    # Draw the current line segment.
    # 'ax.plot' draws a line between two points (x, y) and (x_end, y_end).
    ax.plot([x, x_end], [y, y_end], color='green', linewidth=1)

    # Recursive step: We call 'draw_fractal' multiple times to create
    # new, smaller branches or components of the fractal.
    # For each recursive call, we adjust the starting point, length, angle,
    # and decrease the depth.

    # Define parameters for the next level of recursion.
    # These parameters determine the "rules" of our specific fractal.
    # Here, we're creating a branching pattern similar to a tree.

    # Branch 1:
    # The new starting point is the end of the current line segment.
    # The length is reduced (e.g., 70% of the current length).
    # The angle is adjusted (e.g., rotated 20 degrees counter-clockwise).
    # The depth is decremented by 1.
    new_length = length * 0.7
    new_angle_1 = angle + 20
    draw_fractal(ax, x_end, y_end, new_length, new_angle_1, depth - 1)

    # Branch 2:
    # Similar to Branch 1, but with a different angle adjustment
    # (e.g., rotated 20 degrees clockwise).
    new_angle_2 = angle - 20
    draw_fractal(ax, x_end, y_end, new_length, new_angle_2, depth - 1)

    # Optional: Add a third, straighter branch to make it more complex.
    # This demonstrates that the branching rules can be customized.
    # draw_fractal(ax, x_end, y_end, new_length, angle, depth - 1)


# --- Main Execution Block ---

# This block runs when the script is executed directly.
if __name__ == "__main__":
    # Create a figure and an axes object.
    # A figure is the overall window or page, and axes are the plotting areas within it.
    fig, ax = plt.subplots(figsize=(8, 8)) # Setting figsize for a square plot

    # Set the plot limits and aspect ratio.
    # This ensures the fractal is displayed correctly without distortion.
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_aspect('equal', adjustable='box') # Crucial for correct fractal visualization

    # Hide the axes (optional, for a cleaner look).
    ax.axis('off')

    # --- Example Usage ---
    # Call the 'draw_fractal' function to start generating the fractal.

    # Initial parameters:
    # ax: The axes object to draw on.
    # x, y: The starting point of the fractal (center of the canvas).
    # length: The initial length of the first line segment.
    # angle: The initial angle of the first line segment (0 degrees is horizontal to the right).
    # depth: The maximum recursion depth. Higher values create more intricate fractals.

    start_x = 500
    start_y = 100
    initial_length = 200
    initial_angle = 90  # Start drawing upwards
    recursion_depth = 10 # Adjust this value to control complexity

    draw_fractal(ax, start_x, start_y, initial_length, initial_angle, recursion_depth)

    # Display the plot.
    # 'plt.show()' renders the figure and displays it on the screen.
    plt.title("Recursive Fractal Tree") # Add a title to the plot
    plt.show()