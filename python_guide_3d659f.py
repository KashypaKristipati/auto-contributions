# Header Comment: Learning Objective
# This tutorial will guide you through generating a random maze using a Depth-First Search (DFS)-like algorithm
# and then finding the shortest path through it using Breadth-First Search (BFS).
# You'll learn about representing a grid, basic graph traversal, and path reconstruction.

import random
import collections # For deque, a more efficient queue implementation

class Maze:
    """
    A class to represent and manipulate a maze.
    It handles maze generation using a recursive backtracking (DFS-like) approach
    and pathfinding using Breadth-First Search (BFS).
    """

    def __init__(self, width, height):
        """
        Initializes the maze grid.
        Args:
            width (int): The width of the maze (must be odd for proper wall/path separation).
            height (int): The height of the maze (must be odd).
        """
        # Ensure dimensions are odd. A common requirement for grid-based maze generation
        # where paths are 1-unit thick and walls are 1-unit thick.
        if width % 2 == 0: width += 1
        if height % 2 == 0: height += 1

        self.width = width
        self.height = height
        # Initialize the grid with all walls ('#')
        # Each cell is a character: '#' for wall, ' ' for path, 'S' for start, 'E' for end, 'o' for solution path.
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.start = (1, 1) # Conventionally start at (1,1) for odd-dimensioned mazes
        self.end = (height - 2, width - 2) # Conventionally end at (height-2, width-2)

    def _is_valid(self, r, c):
        """Helper to check if a given coordinate is within maze boundaries."""
        return 0 <= r < self.height and 0 <= c < self.width

    def generate(self):
        """
        Generates the maze structure using a Depth-First Search (DFS) / Recursive Backtracking algorithm.
        This algorithm starts at a cell, randomly moves to an unvisited neighbor,
        and carves a path, effectively creating a "perfect" maze with no loops.
        """
        stack = [] # We use a list as a stack for DFS traversal
        # Start the generation from the 'start' point
        current_r, current_c = self.start
        self.grid[current_r][current_c] = ' ' # Mark the start cell as a path
        stack.append((current_r, current_c))

        # Define potential directions for carving paths.
        # Each step moves 2 units (skipping over a wall)
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)] # Right, Left, Down, Up

        while stack:
            # Get the current cell from the top of the stack (LIFO) without removing it yet
            current_r, current_c = stack[-1]

            # Find unvisited neighbors that are 2 units away (potential cells to carve into)
            unvisited_neighbors = []
            for dr, dc in directions:
                neighbor_r, neighbor_c = current_r + dr, current_c + dc
                # Check if the neighbor is valid and is still a wall (unvisited by path carving)
                if self._is_valid(neighbor_r, neighbor_c) and self.grid[neighbor_r][neighbor_c] == '#':
                    unvisited_neighbors.append((neighbor_r, neighbor_c))

            if unvisited_neighbors:
                # If there are unvisited neighbors, pick one randomly
                next_r, next_c = random.choice(unvisited_neighbors)

                # Carve a path:
                # 1. Mark the chosen neighbor as a path
                self.grid[next_r][next_c] = ' '
                # 2. Carve the wall in between the current cell and the chosen neighbor
                #    The cell in between is (current_r + dr/2, current_c + dc/2)
                wall_r, wall_c = current_r + (next_r - current_r) // 2, current_c + (next_c - current_c) // 2
                self.grid[wall_r][wall_c] = ' '

                # Push the new cell onto the stack and continue DFS
                stack.append((next_r, next_c))
            else:
                # If no unvisited neighbors from the current cell, backtrack by popping it
                stack.pop()

        # Ensure start and end points are explicitly marked after generation
        self.grid[self.start[0]][self.start[1]] = 'S'
        self.grid[self.end[0]][self.end[1]] = 'E'

    def solve(self):
        """
        Finds the shortest path from the start ('S') to the end ('E') using Breadth-First Search (BFS).
        BFS explores all neighbors at the current depth before moving to the next depth,
        guaranteeing the shortest path in an unweighted grid.
        Returns:
            list: A list of (row, col) tuples representing the shortest path, or None if no path exists.
        """
        queue = collections.deque() # Use a deque for efficient queue operations (popleft)
        queue.append(self.start)

        # Store the parent of each cell to reconstruct the path later.
        # This map tracks: `(child_r, child_c)` -> `(parent_r, parent_c)`
        parent_map = {self.start: None}

        # Keep track of visited cells to avoid cycles and redundant processing
        visited = {self.start}

        # Directions for moving to adjacent cells (up, down, left, right)
        # We can only move to cells that are already paths (' ' or 'E')
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

        path_found = False
        while queue:
            current_r, current_c = queue.popleft() # Get the oldest cell in the queue

            if (current_r, current_c) == self.end:
                path_found = True
                break # Found the end, stop searching

            for dr, dc in directions:
                neighbor_r, neighbor_c = current_r + dr, current_c + dc

                # Check if neighbor is valid, is a path (not a wall), and has not been visited
                if (self._is_valid(neighbor_r, neighbor_c) and
                    self.grid[neighbor_r][neighbor_c] != '#' and
                    (neighbor_r, neighbor_c) not in visited):

                    visited.add((neighbor_r, neighbor_c)) # Mark as visited
                    queue.append((neighbor_r, neighbor_c)) # Add to queue for future exploration
                    parent_map[(neighbor_r, neighbor_c)] = (current_r, current_c) # Record its parent

        if not path_found:
            return None # No path found

        # Reconstruct the path by backtracking from the end to the start using the parent_map
        path = []
        current = self.end
        while current is not None:
            path.append(current)
            current = parent_map[current]
        return path[::-1] # Reverse the path to go from start to end

    def display(self, path=None):
        """
        Prints the current state of the maze grid to the console.
        Args:
            path (list, optional): A list of (row, col) tuples representing a solution path
                                   to be drawn on the maze.
        """
        display_grid = [row[:] for row in self.grid] # Create a copy to avoid modifying original grid

        if path:
            # Mark the solution path with 'o' (excluding start and end points)
            for r, c in path:
                if (r, c) != self.start and (r, c) != self.end:
                    display_grid[r][c] = 'o'

        # Print each row of the maze, joining characters to form a single string per row
        for r in range(self.height):
            print("".join(display_grid[r]))

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Generating and Solving a Random Maze ---")

    # Define maze dimensions. It's recommended to use odd numbers for width and height
    # to ensure proper wall/path separation during generation.
    maze_width = 31
    maze_height = 19

    # 1. Create a Maze instance
    my_maze = Maze(maze_width, maze_height)
    print(f"\nInitialized empty {maze_height}x{maze_width} maze:")
    my_maze.display()

    # 2. Generate the maze structure using recursive backtracking (DFS-like)
    my_maze.generate()
    print("\nGenerated random maze:")
    my_maze.display()

    # 3. Find the solution path using Breadth-First Search (BFS)
    solution_path = my_maze.solve()

    # 4. Display the maze with the solution path (if found)
    if solution_path:
        print("\nMaze with solution path ('o'):")
        my_maze.display(solution_path)
        # The path length is the number of steps, which is (number of cells - 1)
        print(f"\nPath length: {len(solution_path) - 1} steps")
    else:
        # This case should ideally not happen for a perfectly generated maze
        # unless start/end are unreachable due to extremely small maze size.
        print("\nNo solution path found.")

    print("\n--- Tutorial Complete ---")