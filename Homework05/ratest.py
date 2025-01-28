def counting_sort(arr, div):
    result = []
    for i in range(10):
        for a in arr:
            index = (a // div) % 10
            if index == i:
                    result.append(a)
                    
    for i in range(len(arr)):
        arr[i] = result[i]
    print(arr)
def radix_sort(arr):
    max_val = max(arr)
    div = 1
    while max_val // div > 0:
        counting_sort(arr, div)
        div *= 10

data = [15, 13, 55, 68, 73, 52, 101, 65, 333, 2, 0, 90, 45, 66, 153, 777]#[170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(data)
print("Sorted Array:", data)