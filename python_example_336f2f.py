# Abstract Visual Art with Python Turtle: Exploring Recursive Patterns

# Learning Objective:
# This tutorial will teach you how to create abstract visual art by
# procedurally generating patterns and shapes using Python's `turtle`
# module. We will focus on the concept of recursion to create
# self-similar, complex designs from simple rules.

import turtle
import random

# --- Setup the Turtle Screen ---

# Create a screen object. This is where our drawing will appear.
screen = turtle.Screen()
# Set the background color of the screen for better contrast.
screen.bgcolor("black")
# Give the window a title.
screen.title("Recursive Art Generator")
# Turn off screen updates to make the drawing process faster.
# We'll update it manually at the end to see the final result.
screen.tracer(0)

# --- Initialize the Turtle ---

# Create a turtle object. This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
# Set the drawing speed. 0 is the fastest.
artist.speed(0)
# Hide the turtle icon while it's drawing to make the art cleaner.
artist.hideturtle()
# Set the initial color of the turtle's pen.
artist.pencolor("cyan")
# Set the thickness of the pen.
artist.pensize(2)

# --- Core Concept: Recursive Drawing ---

# Recursion is a technique where a function calls itself.
# In art, this means we can draw a smaller version of a pattern
# within itself, leading to intricate, self-repeating designs.

def draw_recursive_pattern(turtle_obj, size, depth, angle, color_palette):
    """
    Recursively draws a fractal-like pattern.

    Args:
        turtle_obj (turtle.Turtle): The turtle object to use for drawing.
        size (int): The current size of the shape being drawn.
        depth (int): The current recursion depth. Controls how many levels
                     of recursion are performed.
        angle (int): The angle to turn after drawing a segment.
        color_palette (list): A list of colors to choose from for the pen.
    """

    # Base Case: When to stop recursing.
    # If the depth reaches 0 or the size becomes too small, we stop drawing
    # this branch of the pattern to prevent infinite recursion.
    if depth <= 0 or size < 5:
        return

    # --- Drawing Logic ---

    # Choose a random color from the palette for this segment.
    # This makes each generated piece unique.
    turtle_obj.pencolor(random.choice(color_palette))

    # Draw a line segment of the current size.
    turtle_obj.forward(size)

    # --- Recursive Calls ---

    # To create the fractal effect, we call the function again
    # with modified parameters.

    # 1. First recursive call: Draw a smaller segment to the right.
    #    - size: reduced by 15% (size * 0.85)
    #    - depth: reduced by 1 (depth - 1)
    #    - angle: turn right by the specified angle.
    turtle_obj.right(angle)
    draw_recursive_pattern(turtle_obj, size * 0.85, depth - 1, angle, color_palette)

    # 2. Second recursive call: Draw a smaller segment to the left.
    #    - size: also reduced by 15%.
    #    - depth: reduced by 1.
    #    - angle: turn left by twice the specified angle. This creates
    #             an opposing branch, often resulting in branching or
    #             leaf-like structures.
    turtle_obj.left(angle * 2)
    draw_recursive_pattern(turtle_obj, size * 0.85, depth - 1, angle, color_palette)

    # --- Backtracking ---

    # After drawing the branches, we need to "backtrack" to the position
    # and orientation where this function call started. This is crucial
    # for the next segment or the parent call to draw correctly.

    # Turn back to the original orientation for this call.
    turtle_obj.right(angle)
    # Move back by the same size we moved forward.
    turtle_obj.backward(size)

# --- Example Usage ---

# Define a palette of vibrant colors for our art.
# You can experiment with different color combinations!
my_colors = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4DC0C0", "#4F80E0", "#9775FA"]

# Set initial drawing parameters.
initial_size = 200  # The starting length of the first line segment.
recursion_depth = 8  # How many levels of self-similarity we want.
turn_angle = 30      # The angle for turning at each step.

# Move the turtle to a starting position.
# We want the art to be centered, so we move it to the bottom center.
artist.penup()  # Lift the pen so it doesn't draw while moving.
artist.goto(0, -150)
artist.pendown() # Put the pen down to start drawing.

# Start the recursive drawing process.
draw_recursive_pattern(artist, initial_size, recursion_depth, turn_angle, my_colors)

# --- Finalizing the Art ---

# Update the screen to show the complete drawing.
screen.update()

# Keep the window open until it's manually closed.
screen.mainloop()
# This line will only be reached when the user closes the turtle graphics window.