"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        root_tmp = root
        while root_tmp:
            curr = prev = Node()
            while root_tmp:
                if root_tmp.left:
                    curr.next = root_tmp.left
                    curr = curr.next
                if root_tmp.right:
                    curr.next = root_tmp.right
                    curr = curr.next
                root_tmp = root_tmp.next
            root_tmp = prev.next
               
        return root
