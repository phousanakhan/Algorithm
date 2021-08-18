# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(root, max_val_from_root):
            if root != None:
                if root.val >= max_val_from_root:
                    max_val_from_root = root.val
                    self.good_nodes += 1
                else:
                    print(root.val, "bad node")
                dfs(root.right, max_val_from_root)
                dfs(root.left, max_val_from_root)
                
        self.good_nodes = 0
        max_val_from_root = float('-inf')
        dfs(root, max_val_from_root)
        return self.good_nodes
        
        
            
            
            
            
            
        
