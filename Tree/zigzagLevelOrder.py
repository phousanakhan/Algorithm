# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, 0, result, 1)
        for index, List in enumerate(result):
            if index % 2 == 0:
                result[index] = result[index][::-1]
        return result
    
    def helper(self, root, level, result, direction):
        if root == None:
            return 
        if len(result) <= level:
            result.append([])
            
        result[level].append(root.val)
        
        self.helper(root.right, level+1, result, direction)
        self.helper(root.left, level+1, result, direction)
