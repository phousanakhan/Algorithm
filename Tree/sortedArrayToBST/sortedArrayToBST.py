# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == None:
            return(None)
        else:
            return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums, left, right) -> TreeNode:
        if left > right:
            return None
        
        mid = (left + right) // 2
        newTree = TreeNode(nums[mid])
        newTree.left = self.helper(nums, left, mid - 1)
        newTree.right = self.helper(nums, mid + 1, right)
        
        return(newTree)