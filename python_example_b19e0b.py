# Pixel Art Drawer Tutorial using Tkinter

# Learning Objective:
# This tutorial will teach you the fundamentals of building an interactive graphical
# application using Python's Tkinter library. Specifically, you will learn:
# 1. How to create a basic Tkinter window.
# 2. How to use the Canvas widget for drawing.
# 3. How to handle mouse events (like clicks and drags) to create interactive
#    functionality.
# 4. How to draw simple shapes (rectangles representing pixels) on the canvas.
# 5. How to change the color of these pixels based on user input.

import tkinter as tk

# Define constants for better readability and easier modification
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PIXEL_SIZE = 20 # Each "pixel" in our art will be 20x20 pixels on the screen
GRID_COLOR = "gray" # Color of the grid lines
DEFAULT_COLOR = "white" # Default color for drawing pixels

class PixelArtDrawer:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("Pixel Art Drawer") # Set the window title

        # --- Canvas Setup ---
        # Create a Canvas widget. This is where we'll draw our pixel art.
        self.canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=DEFAULT_COLOR)
        self.canvas.pack() # Place the canvas widget in the window

        # Draw the initial grid on the canvas
        self.draw_grid()

        # --- Event Handling Setup ---
        # Bind mouse events to specific methods.
        # "<Button-1>" is the event for the left mouse button click.
        self.canvas.bind("<Button-1>", self.handle_click)
        # "<B1-Motion>" is the event for moving the mouse while the left button is held down.
        self.canvas.bind("<B1-Motion>", self.handle_drag)

        # --- Color Palette ---
        # For simplicity, we'll use a few predefined colors.
        self.colors = ["black", "red", "blue", "green", "yellow", "purple"]
        self.current_color = self.colors[0] # Start with the first color (black)

        # Create a frame to hold the color buttons
        self.color_frame = tk.Frame(master)
        self.color_frame.pack()

        # Create buttons for each color in our palette
        for color in self.colors:
            # Create a button for the color
            button = tk.Button(self.color_frame, bg=color, width=2, command=lambda c=color: self.set_color(c))
            button.pack(side=tk.LEFT) # Place buttons side-by-side

    def draw_grid(self):
        # This method draws the grid lines on the canvas.
        # We iterate through rows and columns to draw lines.

        # Draw vertical lines
        for x in range(0, CANVAS_WIDTH, PIXEL_SIZE):
            # create_line(x1, y1, x2, y2, fill="color")
            # (x, 0) is the start point, (x, CANVAS_HEIGHT) is the end point
            self.canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill=GRID_COLOR)

        # Draw horizontal lines
        for y in range(0, CANVAS_HEIGHT, PIXEL_SIZE):
            # (0, y) is the start point, (CANVAS_WIDTH, y) is the end point
            self.canvas.create_line(0, y, CANVAS_WIDTH, y, fill=GRID_COLOR)

    def get_pixel_coordinates(self, event):
        # This method calculates which "pixel" (which grid cell) was clicked or dragged over.
        # event.x and event.y are the mouse coordinates relative to the canvas.

        # Integer division (//) is used to find which pixel block the mouse is in.
        # For example, if PIXEL_SIZE is 20 and event.x is 35, then 35 // 20 = 1.
        # This means it's the second pixel block horizontally (index 1).
        pixel_x = (event.x // PIXEL_SIZE) * PIXEL_SIZE
        pixel_y = (event.y // PIXEL_SIZE) * PIXEL_SIZE

        return pixel_x, pixel_y

    def draw_pixel(self, x, y):
        # This method draws a single colored pixel (rectangle) at the given grid coordinates.

        # Calculate the coordinates for the rectangle's bounding box.
        # The top-left corner is (x, y).
        # The bottom-right corner is (x + PIXEL_SIZE, y + PIXEL_SIZE).
        x1 = x
        y1 = y
        x2 = x + PIXEL_SIZE
        y2 = y + PIXEL_SIZE

        # Create a rectangle on the canvas.
        # create_rectangle(x1, y1, x2, y2, fill="color", outline="color")
        # We fill it with the current drawing color and also set the outline to the same color
        # so it blends seamlessly with neighboring pixels.
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)

    def handle_click(self, event):
        # This method is called whenever the left mouse button is clicked on the canvas.
        # It draws a single pixel at the clicked location.
        pixel_x, pixel_y = self.get_pixel_coordinates(event)
        self.draw_pixel(pixel_x, pixel_y)

    def handle_drag(self, event):
        # This method is called whenever the mouse is moved while the left button is held down.
        # It draws a continuous line of pixels as the user drags.
        pixel_x, pixel_y = self.get_pixel_coordinates(event)
        self.draw_pixel(pixel_x, pixel_y)

    def set_color(self, color):
        # This method updates the currently selected drawing color.
        self.current_color = color

# --- Example Usage ---
if __name__ == "__main__":
    # This block runs only when the script is executed directly.

    # Create the main Tkinter window
    root = tk.Tk()

    # Instantiate our PixelArtDrawer class, passing the main window to it
    my_drawer = PixelArtDrawer(root)

    # Start the Tkinter event loop. This makes the window appear and waits for user interactions.
    root.mainloop()