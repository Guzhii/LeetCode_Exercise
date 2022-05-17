# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None
        def DFS(orig, clone):
            if orig != None:
                print(orig.val)
                if orig.val == target.val:
                    self.res = clone
                DFS(orig.left, clone.left)
                DFS(orig.right, clone.right)
                
        DFS (original, cloned)
        return self.res
