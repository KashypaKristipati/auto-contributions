# Greedy Interval Scheduling Algorithm

def max_interval_scheduling(intervals):
    # Sort intervals by end time
    # This is the key insight of the greedy algorithm: we want to schedule the interval with the earliest end time first
    intervals.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the current end time and the scheduled intervals
    current_end_time = 0
    scheduled_intervals = []
    
    for start, end in intervals:
        # If the new interval starts after the current end time, we can schedule it
        if start >= current_end_time:
            current_end_time = end
            scheduled_intervals.append((start, end))
            
    return len(scheduled_intervals)

# Example usage:

intervals = [(1, 5), (2, 4), (3, 6)]
print("Number of intervals scheduled:", max_interval_scheduling(intervals))  # Output: Number of intervals scheduled: 3

intervals = [(1, 10), (2, 8), (3, 7), (4, 5)]
print("Number of intervals scheduled:", max_interval_scheduling(intervals))  # Output: Number of intervals scheduled: 4