# Recursive Backtracking Algorithm for N-Queens Problem

def solve_n_queens(n):
    # Initialize solution and failed attempts lists
    solutions = []
    failed_attempts = []

    def is_valid(board, row, col):
        # Check if placing a queen at (row, col) would be a valid move
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    return False
        return True

    def place_queen(n, row, board, solution):
        # Attempt to place a queen at position (row, col)
        if row == n:
            solutions.append(solution[:])
            return

        for col in range(n):
            if is_valid(board, row, col):
                # Place a queen at (row, col) and try to solve the rest of the board
                board[row] = col
                solution.append(col)
                place_queen(n, row + 1, board, solution)
                # Backtrack: remove the last placed queen from the current solution
                solution.pop()

    def backtrack(n):
        # Start with an empty board and attempt to solve it
        if n == 0:
            return

        for _ in range(n):
            place_queen(n, 0, [None] * n, [])

    # Try all possible initial placements of queens on the board
    for _ in range(8):  
        backtrack(n)

    return solutions


# Example usage
if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print("Solutions:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in range(len(solution)):
            col = solution[row]
            # Represent the board with 'Q' (queen) and '.' (empty space)
            if col == -1:
                print('.', end=' ')
            else:
                print('Q', end=' ')
        print()