def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick(less) + [pivot] + quick(greater)

print(quick([1, 3, 6, 1, 2, 20, -1, -9]))