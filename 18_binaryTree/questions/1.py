"""
You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:

Return the nodes from the leftmost node to the rightmost node.
If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view.
Examples:

Input: root = [1, 2, 3]
Output: [2, 1, 3]
Explanation: The Green colored nodes represents the top view in the below Binary tree.

Input: root = [10, 20, 30, 40, 60, 90, 100]
Output: [40, 20, 10, 30, 100]
Explanation: The Green colored nodes represents the top view in the below Binary tree.


Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105

"""

""" 
                      6 
                   N     2 
                       8    3
                    4     
"""


class Solution:
    def topView(self, root):
        arr = []

        def leftHelper(temp, arr):
            if temp.left != None:
                leftHelper(temp.left, arr)
            if root != temp:
                arr.append(temp.data)
            if len(arr)==0:
                temp=temp.right.left
                leftHelper(temp.left, arr) 
            return arr

        def rightHelper(temp, arr):
            if temp.right != None:
                arr.append(temp.right.data)
                rightHelper(temp.right, arr)  
            return arr

        arr = leftHelper(root, arr)
        arr.append(root.data)
        arr = rightHelper(root, arr) 
        return arr
