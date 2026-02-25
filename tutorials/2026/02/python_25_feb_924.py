# Greedy Interval Scheduling

# Interval class to store start and end times
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Function to find the maximum value using greedy interval scheduling
def find_max_value(intervals):
    # Sort intervals based on their end times
    intervals.sort(key=lambda x: x.end)
    
    # Initialize the maximum value and the end time of the last scheduled interval
    max_value = 0
    last_end = -1
    
    # Iterate over the sorted intervals
    for interval in intervals:
        # If the current interval does not overlap with the last scheduled interval
        if interval.start >= last_end:
            # Update the maximum value and the end time of the last scheduled interval
            max_value = max(max_value, interval.end - interval.start)
            last_end = interval.end
    
    return max_value

# Test the greedy interval scheduling algorithm
intervals = [Interval(1, 3), Interval(2, 4), Interval(3, 5), Interval(6, 7), Interval(8, 9)]
print("Maximum value using greedy interval scheduling:", find_max_value(intervals))

# Test the greedy interval scheduling algorithm with no intervals
intervals = []
print("Maximum value using greedy interval scheduling:", find_max_value(intervals))

# Test the greedy interval scheduling algorithm with one interval
intervals = [Interval(1, 3)]
print("Maximum value using greedy interval scheduling:", find_max_value(intervals))

# Test the greedy interval scheduling algorithm with multiple intervals
intervals = [Interval(1, 3), Interval(2, 4), Interval(3, 5), Interval(4, 6), Interval(5, 7)]
print("Maximum value using greedy interval scheduling:", find_max_value(intervals))