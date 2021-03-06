# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        tempList = []
            
        def helper(root):
            if root and len(tempList)<k:
                helper(root.left)
                tempList.append(root.val)
                helper(root.right)
                
        helper(root)
        
        return tempList[k-1]
