class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    # add first=>
    def addFirst(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode

    # remove first=>
    def removeFirst(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            removedData = self.head.data
            self.head = self.head.next
            print("Removed Data->", removedData)

    # add last=>
    def addLast(self, data):
        newNode = Node(data)
        if self.head == None and self.tail == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    # remove last=>
    def removeLast(self):
        if self.head == None:
            return print("Linked list is empty!")

        if self.head.next == None:
            removedData = self.head.data
            self.head = None
            return print("Removed Data->", removedData)

        temp = self.head
        while temp.next != None and temp.next.next != None:
            temp = temp.next
        removedData = temp.next.data
        temp.next = None
        print("Removed Data->", removedData)

    # print linked lists=>
    def printLinkedList(self):
        temp = self.head
        if temp is None:
            return print("Singly linked list is empty!")
        while temp != None:
            print(temp.data)
            temp = temp.next
