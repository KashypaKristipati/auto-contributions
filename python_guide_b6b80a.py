# Fractal Art with Recursion and Turtle Graphics

# Learning Objective:
# This tutorial will teach you how to create mesmerizing fractal art using
# the power of recursion and Python's built-in turtle graphics module.
# We will focus on understanding how a simple recursive function can generate
# complex and beautiful patterns.

# Import the turtle module, which provides a simple drawing canvas.
import turtle

# Set up the screen for our drawing.
# This creates a window where our fractal will be drawn.
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Set the dimensions of the window.
screen.bgcolor("black")             # Set the background color to black for a dramatic effect.
screen.title("Recursive Fractal Art") # Set the title of the window.

# Create a turtle object.
# This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
artist.speed(0)  # Set the drawing speed to the fastest (0) for quicker rendering.
artist.color("cyan") # Set the drawing color.

# --- The Core Concept: Recursion ---
# Recursion is a programming technique where a function calls itself.
# This is incredibly powerful for creating self-similar patterns, like fractals.
# Think of it like a set of Russian nesting dolls: each doll contains a smaller
# version of itself.

# --- Recursive Function for Drawing a Fractal (e.g., a Sierpinski Triangle) ---

def draw_fractal(level, size):
    """
    This function recursively draws a fractal pattern.

    Args:
        level (int): The current depth of recursion. Controls the complexity.
        size (int): The length of the current line segment to draw.
    """
    # Base Case: The condition that stops the recursion.
    # When the level reaches 0, we stop drawing further.
    # This prevents an infinite loop.
    if level == 0:
        return # Exit the function, stopping this branch of recursion.

    # Recursive Step: The part where the function calls itself.
    # We draw a line and then recursively call draw_fractal for smaller
    # segments and at a deeper level.

    # Draw the current line segment.
    artist.forward(size)

    # Now, we'll branch out. Imagine this as creating three smaller
    # versions of the fractal.

    # First Branch:
    # Turn left, draw a smaller fractal, then turn back.
    artist.left(60) # Turn left by 60 degrees (part of the Sierpinski pattern).
    draw_fractal(level - 1, size * 0.5) # Recursive call: decrease level, halve size.
    artist.right(60) # Turn back to the original orientation.

    # Second Branch:
    # Move forward, draw a smaller fractal, then move back.
    artist.forward(size) # Move forward by the original size to position for the next branch.
    artist.left(60) # Turn left by 60 degrees.
    draw_fractal(level - 1, size * 0.5) # Recursive call.
    artist.right(60) # Turn back.

    # Third Branch:
    # Move back to the starting point of this segment.
    artist.backward(size) # Move back to the original starting point of this segment.
    artist.left(60) # Turn left by 60 degrees to prepare for the next recursive call from the parent.
    draw_fractal(level - 1, size * 0.5) # Recursive call.
    artist.right(60) # Turn back.

# --- Example Usage ---

# Let's set the initial parameters for our fractal.
# 'initial_level' controls the complexity and detail. Higher numbers mean more detail.
# 'initial_size' controls the overall scale of the fractal.
initial_level = 5  # Try changing this to 4, 6, or 7 to see the difference!
initial_size = 200 # Try changing this to 150 or 250.

# Position the turtle to start drawing from the center-bottom of the screen.
artist.penup() # Lift the pen so it doesn't draw while moving.
artist.goto(-initial_size / 2, -initial_size / 2) # Move to a starting position.
artist.pendown() # Put the pen down to start drawing.

# Call the recursive function to generate the fractal art.
# The first call starts the entire process.
draw_fractal(initial_level, initial_size)

# Keep the window open until it's manually closed.
screen.mainloop()

# --- Explanation of the Sierpinski Triangle Structure ---
# The `draw_fractal` function, as implemented, is drawing a variation of
# a Sierpinski triangle. At each level:
# 1. It draws a line segment.
# 2. It branches out three times.
# 3. Each branch makes a recursive call with a smaller size and a reduced level.
# This process continues until the `level` becomes 0 (the base case), at which
# point the recursion stops for that particular branch. The combination of
# these branches creates the self-similar structure.

# --- How to Experiment ---
# - Change `initial_level`:
#   - Lower values (e.g., 3, 4) will be faster and less detailed.
#   - Higher values (e.g., 6, 7) will take longer but produce very intricate patterns.
# - Change `initial_size`: This scales the entire drawing up or down.
# - Modify the angles (`left()`, `right()`): Experiment with different angles to create
#   different fractal shapes (e.g., Koch snowflakes, fractal trees).
# - Change colors: You can change `artist.color()` at different stages to create
#   multi-colored fractals.
# - Explore different base cases: Instead of just `return` at `level == 0`, you could
#   draw a small shape or color a pixel.

# This tutorial provides a foundational understanding of recursion for art.
# Keep experimenting and have fun!