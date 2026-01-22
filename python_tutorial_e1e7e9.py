# Educational Tutorial: Visualizing Fractals with Recursive Turtle Graphics

# Learning Objective:
# This tutorial will teach you how to create visually stunning fractal patterns
# by leveraging the power of recursion and Python's turtle graphics module.
# You will learn how a simple set of rules, applied repeatedly, can generate
# complex and beautiful geometric designs.

# What are Fractals?
# Fractals are self-similar patterns, meaning that they look similar at different
# scales. If you zoom in on a part of a fractal, you'll often see a smaller version
# of the whole pattern. This self-similarity is achieved through a process of
# repetition or recursion.

# What is Recursion?
# Recursion is a programming technique where a function calls itself.
# It's like a set of Russian nesting dolls: each doll contains a smaller,
# identical doll until you reach the smallest one.
# In programming, a recursive function needs two main parts:
# 1. Base Case: A condition that stops the recursion. Without it, the function
#    would call itself forever, leading to a stack overflow error.
# 2. Recursive Step: The part where the function calls itself, usually with
#    modified arguments that bring it closer to the base case.

# How Turtle Graphics Works:
# The `turtle` module in Python provides a simple way to draw graphics.
# You can think of the turtle as a pen that you can move around on a canvas.
# Key commands include:
# - `turtle.forward(distance)`: Moves the turtle forward by a specified distance.
# - `turtle.backward(distance)`: Moves the turtle backward.
# - `turtle.right(angle)`: Turns the turtle clockwise by an angle in degrees.
# - `turtle.left(angle)`: Turns the turtle counter-clockwise.
# - `turtle.penup()`: Lifts the pen, so subsequent movements don't draw.
# - `turtle.pendown()`: Puts the pen down, so movements will draw.
# - `turtle.speed(speed_value)`: Sets the drawing speed (0 is fastest, 1-10 are slow to fast).
# - `turtle.Screen()`: Gets the drawing screen object to manage the window.

# Let's get started with our first fractal: the Koch Snowflake Curve.
# The Koch snowflake is created by starting with an equilateral triangle,
# and then repeatedly applying a rule to each line segment.
# The rule is: divide the segment into three equal parts, remove the middle
# part, and replace it with two segments of the same length, forming an
# outward-pointing equilateral triangle.

import turtle

# --- Function Definitions ---

def draw_koch_segment(t, order, size):
    """
    Recursively draws a single Koch curve segment of a given order and size.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        order (int): The current recursion depth. This determines the complexity
                     of the fractal. A higher order means more detail.
        size (float): The length of the current segment to draw.
    """
    # Base Case: If the order is 0, we just draw a straight line segment.
    # This is the simplest form of the Koch curve.
    if order == 0:
        t.forward(size)
        return # Stop the recursion for this branch

    # Recursive Step: If the order is greater than 0, we break the segment
    # into four smaller segments and recursively call the function for each.

    # Divide the current segment into three equal parts.
    smaller_size = size / 3.0

    # 1. Draw the first third of the segment.
    draw_koch_segment(t, order - 1, smaller_size)

    # 2. Turn left by 60 degrees and draw the second part (the outward triangle peak).
    t.left(60)
    draw_koch_segment(t, order - 1, smaller_size)

    # 3. Turn right by 120 degrees (60 + 60) to face the correct direction
    #    for the third part.
    t.right(120)
    draw_koch_segment(t, order - 1, smaller_size)

    # 4. Turn left by 60 degrees to face the correct direction for the fourth part.
    t.left(60)
    draw_koch_segment(t, order - 1, smaller_size)

def draw_koch_snowflake(t, order, size):
    """
    Draws the complete Koch snowflake by calling draw_koch_segment three times.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        order (int): The recursion order for each segment of the snowflake.
        size (float): The initial length of each side of the triangle.
    """
    # The Koch snowflake is formed by three Koch curves arranged in an equilateral triangle.
    # We call our recursive function three times, turning 120 degrees between each call.
    for _ in range(3):
        draw_koch_segment(t, order, size)
        t.right(120) # Turn 120 degrees to draw the next side of the triangle.

# --- Main Execution Block ---

if __name__ == "__main__":
    # This block of code will only run when the script is executed directly
    # (not when it's imported as a module).

    # 1. Set up the screen and turtle.
    screen = turtle.Screen()
    screen.setup(width=800, height=600) # Set the window size.
    screen.bgcolor("white")            # Set the background color.
    screen.title("Koch Snowflake Fractal") # Set the window title.

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)       # Set the fastest drawing speed (0).
    my_turtle.penup()        # Lift the pen to move without drawing.
    my_turtle.goto(-150, 50) # Move the turtle to a starting position.
    my_turtle.pendown()      # Put the pen down to start drawing.
    my_turtle.pencolor("blue") # Set the pen color.
    my_turtle.hideturtle()   # Hide the turtle icon for a cleaner look.

    # 2. Define fractal parameters.
    # 'order' controls the level of detail. Higher order means more intricate patterns
    # but also more computation and longer drawing times.
    # 'size' controls the overall scale of the fractal.
    fractal_order = 4  # You can change this value (e.g., 1, 2, 3, 4, 5)
    initial_size = 300 # You can change this value

    # 3. Draw the fractal.
    print(f"Drawing Koch Snowflake with order {fractal_order} and size {initial_size}...")
    draw_koch_snowflake(my_turtle, fractal_order, initial_size)
    print("Drawing complete!")

    # 4. Keep the window open until it's manually closed.
    screen.mainloop()