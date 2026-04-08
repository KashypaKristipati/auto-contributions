# Recursive Backtracking for N-Queens Problem

def solve_n_queens(n):
    # Initialize solution set
    solutions = []
    
    def is_safe(board, row, col):
        # Check if queen can be placed on the current position
        for i in range(row):
            # If any queen is found on the same column or diagonals
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True
    
    def backtrack(board, row):
        # Base case: if all queens are placed
        if row == n:
            solution = ''.join(['Q' if i == j else '.' for i in range(n) for j in range(n)])
            solutions.append(solution)
            return
        
        # Try placing a queen at each column of the current row
        for col in range(n):
            # Check if it's safe to place a queen on this position
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                backtrack(board, row + 1)  # Recursively try next row
                
                # If we didn't find any solution for the current board,
                # then remove the queen from the last column of the current row
                board[row] = None
    
    # Start backtracking with an empty board
    board = [-1] * n
    backtrack(board, 0)
    
    return solutions

def main():
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-Queens problem:", len(solutions))
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}: {solution}")

if __name__ == "__main__":
    main()