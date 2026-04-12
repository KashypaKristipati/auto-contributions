# Recursive Backtracking in Python
=====================================

Recursive backtracking is an algorithmic technique used to solve constraint satisfaction problems and other combinatorial optimization problems.
This implementation uses a recursive function with backtracking to find solutions that satisfy given rules.

```python
def backtrack(start, path, target):
    """
    Recursive backtrack function.

    Args:
        start (int): Starting index for the current branch.
        path (list): List of numbers in the current solution.
        target (int): Target sum for the current solution.
    """
    # Add the next number to the path and recursively call backtrack
    if target == 0:
        result.append(path[:])
        return
    for i in range(start, len(nums)):
        # Check if adding the current number exceeds the target
        if i > start and nums[i] == nums[i-1]:
            continue
        # Add the current number to the path and recursively call backtrack
        path.append(nums[i])
        backtrack(i + 1, path, target - nums[i])
        # Remove the last added number from the path for backtracking
        path.pop()


def solve(nums, target):
    """
    Solve the problem using recursive backtracking.

    Args:
        nums (list): List of numbers.
        target (int): Target sum.

    Returns:
        list: List of solutions that satisfy the given rules.
    """
    result = []
    backtrack(0, [], target)
    return result


# Example usage
nums = [1, 2, 3]
target = 4
result = solve(nums, target)
for i, path in enumerate(result):
    print(f"Solution {i+1}: {path}")