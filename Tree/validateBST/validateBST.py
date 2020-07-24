# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return  self.validate(root, None, None)
    
    def validate(self, root: TreeNode, max: int, min: int):
        if root == None:
            return(True)
        elif ((max != None and max <= root.val) or (min!=None and min >= root.val)):
            return(False)
        else:
            return(self.validate(root.left, root.val, min) and self.validate(root.right, max, root.val))
    