# Fractal Art with Turtle Graphics and Recursion
#
# Learning Objective: This tutorial will teach you how to create
# mesmerizing fractal art using Python's turtle graphics module
# and the powerful concept of recursion. You will learn:
# 1. How to use Python's turtle module for drawing.
# 2. The fundamental concept of recursion: a function calling itself.
# 3. How to apply recursion to create self-similar geometric patterns.
# 4. How to control the complexity and appearance of fractals.
#
# By the end, you'll be able to generate simple fractal trees,
# which are a great visual example of recursive structures.

import turtle

# --- Function to draw a fractal tree ---
# This is the core of our fractal art generation.
# It uses recursion to draw branches that get smaller and smaller.

def draw_fractal_tree(t, branch_length, angle, depth):
    """
    Recursively draws a fractal tree.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        branch_length (float): The length of the current branch.
        angle (float): The angle at which the branches split.
        depth (int): The current recursion depth (controls complexity).
    """
    # Base Case: When the depth reaches 0, we stop drawing branches.
    # This is crucial to prevent infinite recursion and is the
    # stopping point for our recursive calls.
    if depth == 0:
        return

    # Draw the current branch
    # This is the "action" part of the recursive step.
    t.forward(branch_length)

    # Store the current position and heading
    # We need to remember where we are before we branch off,
    # so we can return to this point and draw the other branch.
    current_pos = t.position()
    current_heading = t.heading()

    # --- Recursive Step: Draw the left branch ---
    # Turn left by the specified angle.
    t.left(angle)
    # Recursively call draw_fractal_tree for the left branch.
    # The branch length is reduced (e.g., by 2/3), and the depth is decreased by 1.
    # This makes the new branches smaller and moves us closer to the base case.
    draw_fractal_tree(t, branch_length * 0.7, angle, depth - 1)

    # --- Return to the junction and draw the right branch ---
    # Restore the position and heading to where we were before the left branch.
    # This is essential for drawing the right branch from the same starting point.
    t.penup() # Lift the pen so we don't draw while moving back
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown() # Put the pen down to draw the right branch

    # Turn right by the specified angle.
    t.right(angle)
    # Recursively call draw_fractal_tree for the right branch.
    # Similar to the left branch, reducing length and depth.
    draw_fractal_tree(t, branch_length * 0.7, angle, depth - 1)

    # --- Return to the parent branch ---
    # After drawing both sub-branches, we need to return to the
    # end of the parent branch to allow further recursion up the tree.
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()

# --- Example Usage ---
# This section shows how to set up the turtle and call our fractal function.

if __name__ == "__main__":
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black") # Dark background makes the green/brown branches pop

    # Create a turtle object
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)  # Set speed to fastest (0) for quick drawing
    my_turtle.color("green") # Set the initial branch color
    my_turtle.pensize(2) # Make the branches a bit thicker

    # Position the turtle at the bottom center of the screen
    my_turtle.penup()
    my_turtle.goto(0, -250)
    my_turtle.pendown()
    my_turtle.setheading(90) # Point the turtle upwards

    # Define the initial parameters for the fractal tree
    initial_branch_length = 100
    branch_split_angle = 30 # The angle between branches
    recursion_depth = 10   # Controls how many levels of branches are drawn

    # Call the function to draw the fractal tree
    # This is where the recursion starts!
    draw_fractal_tree(my_turtle, initial_branch_length, branch_split_angle, recursion_depth)

    # Hide the turtle when drawing is complete for a cleaner look
    my_turtle.hideturtle()

    # Keep the window open until it's manually closed
    screen.mainloop()