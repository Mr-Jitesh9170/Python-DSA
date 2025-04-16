# Min Heap =>
# 1. A Min Heap follows the rules of a Complete Binary Tree and is implemented using an array.
# 2. In a Min Heap, the root element is always smaller than or equal to its children.
# 3. The smallest value in a Min Heap is always at the root node.
# 4. Using a Min Heap, we can implement a Min Priority Queue where smaller values have higher priority.
# 5. To create a Min Priority Queue, we first build a Min Heap, then repeatedly delete the root element and store it.
#    The stored elements form the priority queue in ascending order.
# 6. If we want to sort an array in ascending order, we can use a Min Heap. This is known as Heap Sort, which has a time complexity of O(n log n).
# 7. Building the heap takes O(n) time using heapify (for an entire array).
# 8. Deleting all elements one by one from the heap takes O(n log n) time in total.
# 9. A Priority Queue can be implemented using either a Min Heap or a Min Heap, depending on whether we want maximum or minimum priority.

minHeap = []


# insertion in min heap =>
def insertMinHeap(data):
    minHeap.append(data)
    i = len(minHeap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if minHeap[parent] > minHeap[i]:
            temp = minHeap[parent]
            minHeap[parent] = minHeap[i]
            minHeap[i] = temp
            i = parent
        else:
            break


# deletion in min heap =>

minPriorityQueue = []


def deleteMinHeap():
    if len(minHeap) == 0:
        return "Min heap is empty!"
    elif len(minHeap) == 1:
        deletedData = minHeap.pop()
        minPriorityQueue.append(deletedData)
    else:
        deletedData = minHeap[0]
        minHeap[0] = minHeap.pop()
        minPriorityQueue.append(deletedData)

        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            small = i

            if left < len(minHeap) and minHeap[left] < minHeap[small]:
                small = left
            if right < len(minHeap) and minHeap[right] < minHeap[small]:
                small = right

            if small != i:
                minHeap[i], minHeap[small] = minHeap[small], minHeap[i]
                i = small
            else:
                break


# peek in min heap =>
def peekMinHeap():
    if len(minHeap) == 0:
        return "Min heap is empty!"
    else:
        return minHeap[0]


insertMinHeap(3)
insertMinHeap(2)
insertMinHeap(1)
deleteMinHeap()
print(minHeap, " =====> ", minPriorityQueue)
