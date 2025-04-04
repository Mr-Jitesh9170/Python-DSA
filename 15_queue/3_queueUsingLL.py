# Queue Implementation using linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def add(self, data):
        newData = Node(data)
        if self.head == None:
            self.head = self.tail = newData
        else:
            self.tail.next = newData
            self.tail = newData

    def remove(self):
        if self.isEmpty():
            return -1
        else:
            remData = self.head.data
            self.head = self.head.next
            return remData

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.head.data

    def printQueue(self):
        if self.isEmpty():
            return print("Queue is empty!")
        else:
            temp = self.head
            while temp != None:
                print(temp.data)
                temp = temp.next


q = Queue()

q.add(1)
q.add(2)
q.add(3)
q.printQueue()

q.remove()
print(q.isEmpty())
print(q.peek())
q.printQueue()
