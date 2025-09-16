# In-Order =>
# Rule=>
"""Left ---> Root ----> Right"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        temp = self.root
        isTrue = True

        def helper(temp, data, isTrue):
            if temp == None and isTrue == False:
                return
            
            if temp == None and isTrue:
                temp = Node(data)
                isTrue = False
                return 

            if temp.left == None and isTrue and temp.left.data != -1:
                temp.left = Node(data)
                isTrue = False
            helper(temp.left, data, isTrue)

            if temp.right == None and isTrue and temp.right.data == -1:
                temp.right = Node(data)
            helper(temp.right, data, isTrue)

        helper(temp, data, isTrue)

    # traversal
    def inOrder(self):
        root = self.root

        def helper(root):
            if root == None:
                return
            if root.left != None:
                helper(root.left)
            print(root.data)
            if root.right != None:
                helper(root.right)

        helper(root)
