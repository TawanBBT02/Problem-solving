def counting_sort(arr, div):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // div) % 10
        count[index] += 1
    print(count)

    for i in range(1, 10):
        count[i] += count[i - 1]
    print(count)

    for i in reversed(range(n)):
        index = (arr[i] // div) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
    print(output)

def radix_sort(arr):
    max_num = max(arr)
    div = 1
    while max_num // div > 0:
        counting_sort(arr, div)
        div *= 10

data = [171, 45, 75, 91, 802, 24, 2, 66]
radix_sort(data)
print("Sorted Array:", data)