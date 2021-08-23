# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        self.seen_element = {}
        self.true = False
        def iterator(root, k):
            if root != None:
                rightTree = iterator(root.right, k)
                diff = k - root.val
                if diff in self.seen_element:
                    self.true = True
                else:
                    self.seen_element[root.val] = root.val
                leftTree = iterator(root.left, k)

                
        iterator(root, k)
        return self.true
        
        
        
            
        
