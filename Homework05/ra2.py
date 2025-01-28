def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array (digits 0-9)

    # Count the occurrences of each digit at exp's place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to contain position of the next digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array back to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)

    # Apply counting sort for each digit
    exp = 1  # exp is 10^i (i is the digit place)
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)