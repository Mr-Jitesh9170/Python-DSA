class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root == newNode
            return 
        def helper(temp, newNode):
            if temp.left == None and newNode.data < temp.data:
                temp.left = newNode
                return
            helper(temp.left, newNode)

            if temp.right == None and newNode.data > temp.data:
                temp.righ = newNode
                return
            helper(temp.right, newNode)

    def traverse(self):
        temp = self.root 
        def helper(temp):
            if temp == None:
                print(temp)
                return
            if temp != None:
                print(temp.data, " ")
            helper(temp.left)
            helper(temp.right) 
        helper(temp)


bst = BST()

for i in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(i)
    
bst.traverse()
