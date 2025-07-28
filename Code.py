import random
import time
import sys
sys.setrecursionlimit(3000)  # Increase recursion limit to avoid RecursionError
# Deterministic Quicksort (uses first element as pivot)
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)
# Randomized Quicksort (uses random pivot)
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr.remove(pivot)  # important to remove only one instance of pivot
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)
# Timing utility
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return round((end - start) * 1000, 2)  # Return time in ms
# Test datasets
datasets = {
    "Random": random.sample(range(1, 1001), 1000),
    "Sorted": list(range(1, 1001)),
    "Reverse": list(range(1000, 0, -1))
}
# Measure and print results
print(f"{'Input Type':<15}{'Deterministic (ms)':<20}{'Randomized (ms)':<20}")
for dtype, data in datasets.items():
    try:
        dt_time = measure_time(deterministic_quicksort, data)
    except RecursionError:
        dt_time = "RecursionError"
    try:
        rand_time = measure_time(randomized_quicksort, data)
    except RecursionError:
        rand_time = "RecursionError"
    print(f"{dtype:<15}{str(dt_time):<20}{str(rand_time):<20}")
