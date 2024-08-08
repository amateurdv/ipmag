def find_peak_element(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]
    return "No peak element found"

# Example usage
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
peak_element = find_peak_element(arr)
print("Peak element:", peak_element)
