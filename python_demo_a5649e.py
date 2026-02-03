# Learning Objective: Programmatically Create Abstract Visual Art
# This tutorial will guide you through creating simple abstract visual art
# using Python and the Matplotlib plotting library. We will focus on
# the concept of layering and blending colors and shapes to create
# emergent visual patterns.

# Import the necessary library for plotting.
# Matplotlib is a powerful and widely-used plotting library in Python.
import matplotlib.pyplot as plt
# We'll also import NumPy for numerical operations, especially for generating random numbers.
import numpy as np

# Define a function to generate a single abstract art element.
# This function will encapsulate the logic for creating one "stroke" or shape.
def create_art_element(ax, color, alpha, size, x_range, y_range):
    # 'ax' is the Matplotlib Axes object we'll draw on.
    # 'color' is the color of the element (e.g., 'red', '#FF5733').
    # 'alpha' controls transparency (0.0 is fully transparent, 1.0 is fully opaque).
    # 'size' determines the general scale of the element.
    # 'x_range' and 'y_range' define the area where the element can be placed.

    # Generate random coordinates for the center of our element.
    # np.random.uniform generates random numbers within a specified range.
    center_x = np.random.uniform(x_range[0], x_range[1])
    center_y = np.random.uniform(y_range[0], y_range[1])

    # Generate a random shape type.
    # For this simple example, we'll choose between circles and rectangles.
    shape_type = np.random.choice(['circle', 'rectangle'])

    # Add the shape to the plot.
    if shape_type == 'circle':
        # For a circle, we use plt.Circle.
        # 'radius' is the size of the circle.
        # 'color' and 'alpha' are set as provided.
        # 'fill=True' means the circle will be filled with color.
        circle = plt.Circle((center_x, center_y), radius=size, color=color, alpha=alpha, fill=True)
        # Add the created circle patch to the axes.
        ax.add_patch(circle)
    else: # shape_type == 'rectangle'
        # For a rectangle, we use plt.Rectangle.
        # We need to specify the bottom-left corner (center_x - size/2, center_y - size/2)
        # and the width and height (both 'size' for a square).
        # 'angle' can be used to rotate rectangles, but we'll keep it simple for now.
        rect = plt.Rectangle((center_x - size/2, center_y - size/2), size, size, color=color, alpha=alpha, fill=True)
        # Add the created rectangle patch to the axes.
        ax.add_patch(rect)

# Define the main function to orchestrate the art creation.
def generate_abstract_art(num_elements=50, output_filename="abstract_art.png"):
    # 'num_elements' is the total number of shapes we want to draw.
    # 'output_filename' is where we'll save the generated image.

    # Create a figure and an axes.
    # A figure is the overall window or page, and axes is the area where we plot.
    fig, ax = plt.subplots(figsize=(10, 8)) # Set figure size for better aspect ratio

    # Define the plotting area boundaries.
    # This is the canvas for our art.
    x_bounds = (0, 10)
    y_bounds = (0, 10)

    # Set the limits of the axes to match our defined boundaries.
    # This ensures our art fits within the intended space.
    ax.set_xlim(x_bounds)
    ax.set_ylim(y_bounds)

    # Remove the axis ticks and labels for a cleaner art canvas.
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Optional: Set a background color for the canvas.
    # This adds another layer to our abstract art.
    fig.patch.set_facecolor('#f0f0f0') # A light grey background

    # Generate a palette of colors to use.
    # We can pre-define a list of colors or generate them randomly.
    # Using hex codes for more control.
    color_palette = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]

    # Loop to create each art element.
    for _ in range(num_elements):
        # Randomly select a color from our palette.
        chosen_color = np.random.choice(color_palette)
        # Randomly select a transparency level.
        chosen_alpha = np.random.uniform(0.3, 0.8) # Between 30% and 80% opaque
        # Randomly select a size for the element.
        chosen_size = np.random.uniform(0.5, 2.0) # Element sizes between 0.5 and 2.0 units

        # Call our function to create and add an element to the plot.
        create_art_element(ax, chosen_color, chosen_alpha, chosen_size, x_bounds, y_bounds)

    # Adjust layout to prevent labels/titles from overlapping.
    # This is good practice for any Matplotlib plot.
    plt.tight_layout()

    # Save the generated art to a file.
    # 'dpi' controls the resolution of the saved image.
    plt.savefig(output_filename, dpi=300)
    print(f"Abstract art saved to {output_filename}")

# --- Example Usage ---
# This section shows how to call the function to generate art.

if __name__ == "__main__":
    # Generate abstract art with default settings (50 elements, saved as abstract_art.png).
    generate_abstract_art()

    # You can also customize the number of elements and the output filename.
    # generate_abstract_art(num_elements=100, output_filename="more_complex_art.jpg")

    # To display the plot interactively instead of just saving it, uncomment the line below:
    # plt.show()
    # Note: plt.show() should generally be called *after* plt.savefig() if you want both.