# Max Heap =>
# 1. A Max Heap follows the rules of a Complete Binary Tree and is implemented using an array.
# 2. In a Max Heap, the root element is always greater than or equal to its children.
# 3. The greatest value in a Max Heap is always at the root node.
# 4. Using a Max Heap, we can implement a Max Priority Queue where higher values have higher priority.
# 5. To create a Max Priority Queue, we first build a Max Heap, then repeatedly delete the root element and store it.
#    The stored elements form the priority queue in descending order.
# 6. If we want to sort an array in descending order, we can use a Max Heap. This is known as Heap Sort, which has a time complexity of O(n log n).
# 7. Building the heap takes O(n) time using heapify (for an entire array).
# 8. Deleting all elements one by one from the heap takes O(n log n) time in total.
# 9. A Priority Queue can be implemented using either a Max Heap or a Min Heap, depending on whether we want maximum or minimum priority.



# Operation in max heap =>
# 1. Insert in max heap.
# 2. Deletion in max heap.
# 3. Peek/Root element.


maxHeap = []


# instertion in max heap =>
def insertMaxHeap(data):
    maxHeap.append(data)
    i = len(maxHeap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if maxHeap[parent] < maxHeap[i]:
            temp = maxHeap[parent]
            maxHeap[parent] = maxHeap[i]
            maxHeap[i] = temp
            i = parent
        else:
            break


# deletion in max heap =>
sorted = []


def deleteMaxHeap():
    length = len(maxHeap)
    if length == 0:
        return print("Max heap is empty!")
    if length == 1:
        deleteData = maxHeap[0]
        sorted.append(deleteData)
        maxHeap.pop()
    else:
        deleteData = maxHeap[0]
        sorted.append(deleteData)
        lastData = maxHeap.pop()
        maxHeap[0] = lastData
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            great = i
            if left < len(maxHeap) and maxHeap[left] > maxHeap[great]:
                great = left

            if right < len(maxHeap) and maxHeap[right] > maxHeap[great]:
                great = right

            if i != great:
                maxHeap[i], maxHeap[great] = maxHeap[great], maxHeap[i]
                i = great
            else:
                break


# Peek element in max heap =>
def peekMaxHeap():
    if len(maxHeap) == 0:
        return "Max heap is empty!"
    else:
        return maxHeap[0]

insertMaxHeap(1)
insertMaxHeap(2)
insertMaxHeap(3)
insertMaxHeap(4)
deleteMaxHeap()
print(maxHeap, " ====> ", sorted)
print(peekMaxHeap())