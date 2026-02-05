# Pixel Art Editor Tutorial

# Learning Objective:
# This tutorial will teach you how to build a simple command-line pixel art editor
# in Python. We will focus on:
# 1. Representing a 2D grid (our canvas) using a list of lists.
# 2. Handling user input to draw pixels on the canvas.
# 3. Displaying the canvas in the terminal.
# This will provide a foundational understanding of working with grids and user interaction in Python.

import os # Import the 'os' module for clearing the screen

def clear_screen():
    # This function clears the terminal screen.
    # It's useful for making the art editor feel more interactive by redrawing the canvas.
    # 'nt' is for Windows, 'posix' is for macOS/Linux.
    os.system('cls' if os.name == 'nt' else 'clear')

def create_canvas(width, height, default_char='.'):
    # This function creates our pixel art canvas.
    # We represent the canvas as a list of lists.
    # Each inner list represents a row, and each element in the inner list is a pixel.
    # 'default_char' is the character that will fill the canvas initially (like a blank space).
    canvas = []
    for _ in range(height):
        # For each row, create a list filled with the default character.
        row = [default_char] * width
        canvas.append(row)
    return canvas

def display_canvas(canvas):
    # This function prints the current state of our canvas to the terminal.
    # We iterate through each row and then each character in the row, printing them.
    # 'end=""' prevents 'print' from adding a newline after each character, keeping pixels on the same line.
    for row in canvas:
        for pixel in row:
            print(pixel, end="")
        print() # Print a newline after each row to format the grid correctly.

def draw_pixel(canvas, x, y, color_char):
    # This function allows us to draw a pixel at specific coordinates.
    # 'x' is the column (horizontal position), and 'y' is the row (vertical position).
    # We need to ensure the coordinates are within the bounds of our canvas.
    height = len(canvas)
    width = len(canvas[0]) if height > 0 else 0

    if 0 <= y < height and 0 <= x < width:
        # If the coordinates are valid, update the character at that position.
        canvas[y][x] = color_char
    else:
        # If the coordinates are out of bounds, inform the user.
        print("Error: Coordinates are out of bounds!")

def get_user_command():
    # This function prompts the user for their next action and returns it.
    # We expect commands like "draw R C CHAR" or "quit".
    command_input = input("Enter command (e.g., 'draw 5 3 X' or 'quit'): ").strip().lower()
    return command_input

def parse_command(command_str):
    # This function takes the raw user input and breaks it down into meaningful parts.
    parts = command_str.split()
    command_type = parts[0] if parts else ""

    if command_type == "draw":
        # If the command is "draw", we expect 3 more parts: row, column, and character.
        if len(parts) == 4:
            try:
                # Convert row and column to integers.
                row = int(parts[1])
                col = int(parts[2])
                color = parts[3] # The character to draw
                return ("draw", row, col, color)
            except ValueError:
                # Handle cases where row or column are not valid numbers.
                return ("error", "Invalid row or column number.")
        else:
            # Handle cases where the "draw" command doesn't have the correct number of arguments.
            return ("error", "Invalid 'draw' command format. Use 'draw R C CHAR'.")
    elif command_type == "quit":
        # If the command is "quit", we just return the command type.
        return ("quit",)
    else:
        # If the command is not recognized, return an error.
        return ("error", "Unknown command.")

# --- Main Editor Loop ---

def run_editor(width, height):
    # This is the main function that runs our pixel art editor.
    # It initializes the canvas and then enters a loop to handle user commands.
    canvas = create_canvas(width, height) # Create a blank canvas

    while True: # This is our main game loop. It continues until explicitly broken.
        clear_screen() # Clear the console for a fresh display.
        print("--- Pixel Art Editor ---")
        display_canvas(canvas) # Show the current state of the canvas.
        print("----------------------")

        command_str = get_user_command() # Get input from the user.
        parsed_command = parse_command(command_str) # Process the input.
        command_type = parsed_command[0] # Get the type of command.

        if command_type == "draw":
            # If the command is "draw", unpack the arguments and call draw_pixel.
            # Remember: Our internal coordinates are (x, y) which corresponds to (column, row).
            # User input is often R C, so we map R to y and C to x.
            row_idx = parsed_command[1]
            col_idx = parsed_command[2]
            color = parsed_command[3]
            draw_pixel(canvas, col_idx, row_idx, color) # Call our drawing function.
        elif command_type == "quit":
            # If the command is "quit", print a goodbye message and break the loop.
            print("Exiting editor. Goodbye!")
            break
        elif command_type == "error":
            # If there was an error parsing the command, display the error message.
            print(f"Error: {parsed_command[1]}")
            input("Press Enter to continue...") # Pause so the user can see the error.

# --- Example Usage ---
# This section demonstrates how to start the editor.
# You can change the width and height here to create different sized canvases.
if __name__ == "__main__":
    # The 'if __name__ == "__main__":' block ensures this code only runs when the script is executed directly,
    # not when it's imported as a module into another script.
    CANVAS_WIDTH = 30
    CANVAS_HEIGHT = 15
    run_editor(CANVAS_WIDTH, CANVAS_HEIGHT)