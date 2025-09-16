class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def levelOrder(self, root):
        temp = root
        traversed = [temp]
        while len(traversed) != 0:
            if traversed[0] != None:
                print(traversed[0].data)
                traversed.append(traversed[0].left)
                traversed.append(traversed[0].right)
                traversed.pop(0)
            else:
                traversed.pop(0)


bt = Solution()
bt.levelOrder(bt.root)
