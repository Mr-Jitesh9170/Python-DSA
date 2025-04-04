class Queue:
    def __init__(self):
        self.arr = []
        self.top = -1

    def add(self, data):
        self.arr.append(data)

    def remove(self):
        if self.isEmpty() is not True:
            self.top -= 1
            remData = self.arr[0]
            for i in range(len(self.arr) - 1):
                self.arr[i] = self.arr[i + 1]
            return remData
        else:
            return -1

    def isEmpty(self):
        return self.top == -1

    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.top]

    def printQueue(self):
        for i in self.arr:
            print(i)


q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4) 
print(q.peek()) 