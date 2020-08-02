# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
staticList1 = []
class Solution:
    def levelOrder(self, root: TreeNode):
        finalList = []
        if root == None:
            return(None)
        height = self.maxDepth(root)
        for level in range(height):
            tempList = []
            level += 1
            self.printGivenTree(root, level)
            for i in staticList1:
                tempList.append(i)
            del staticList1[:]
            finalList.append(tempList)
        return(finalList)

    def printGivenTree(self, tree: TreeNode, level: int):
        if tree == None:
            return
        if level == 1:
            staticList1.append(tree.val)
        elif level > 1:
            self.printGivenTree(tree.left, level-1)
            self.printGivenTree(tree.right, level-1)
        
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return(0)
        else:
            maxDepthRight = self.maxDepth(root.right)
            maxDepthLeft = self.maxDepth(root.left)
            if maxDepthRight > maxDepthLeft:
                return(maxDepthRight+1)
            else:
                return(maxDepthLeft+1)