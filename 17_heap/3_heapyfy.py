arr = [ 2, 5, 7, 6,4,9]


def heapify(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(arr)
        heapify(arr, largest, n)


n = len(arr)
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, i, n)
