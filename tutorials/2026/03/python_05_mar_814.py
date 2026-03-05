# Greedy Interval Scheduling

def greedy_interval_scheduling(intervals):
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    # Initialize result with first interval
    result = [intervals[0]]

    # Iterate over intervals
    for start, end in intervals[1:]:
        # Get last scheduled interval
        last_start, last_end = result[-1]

        # Check if current interval overlaps with last scheduled interval
        if start < last_end:
            # Update end time of last scheduled interval
            result[-1] = (last_start, max(last_end, end))
        else:
            # Schedule current interval
            result.append((start, end))

    return result

# Example usage
intervals = [(1, 5), (2, 4), (3, 6), (7, 9), (8, 10), (12, 15)]
schedules = greedy_interval_scheduling(intervals)

# Print schedules
for i, schedule in enumerate(schedules):
    print(f"Scheduling {i+1}:")
    for start, end in schedule:
        print(f"  ({start}, {end})")
    print()