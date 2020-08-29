# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(preorder)-1, preorder, inorder)
    
    def helper(self, rootIndex:int, inStart:int, inEnd:int, preorder:List[int], inorder:List[int]):
        if (rootIndex > len(preorder)-1 or inStart > inEnd):
            return None
        
        newTree = TreeNode(preorder[rootIndex])
        inIndex = 0
        for i in range(inStart, inEnd+1):
            if (newTree.val == inorder[i]):
                inIndex = i 
                
        newTree.left = self.helper(rootIndex+1, inStart, inIndex-1, preorder, inorder)
        newTree.right = self.helper(rootIndex+inIndex-inStart+1, inIndex+1, inEnd, preorder, inorder)
        
        return newTree
