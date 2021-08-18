# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0
        arr_target = []
        self.getArrTarget(root, arr_target)
        tempRoot = root
        visitedNodeList = {}
        for i in range(0, len(arr_target)):
            path = []
            if self.goodNodesGivenTarget(tempRoot, arr_target[i], path, visitedNodeList) == True:
                isGood = True
                for i in range(0, len(path)):
                    if path[i] > path[-1]:
                        isGood = False
                        break
                if isGood == True:
                    good_node += 1
            tempRoot = root
        return good_node
        
    def getArrTarget(self, root, arr_target):
        tempRoot = root
        good_nodes = 0
        if root != None:
            arr_target.append(root.val)
            self.getArrTarget(root.left, arr_target)
            self.getArrTarget(root.right, arr_target)
        
    
    def goodNodesGivenTarget(self, root, target, arr, visitedNodeList):
        if root == None:
            return False
        arr.append(root.val)
        
        if root.val == target and root not in visitedNodeList:
            #visitedNodeList.append(root)
            visitedNodeList[root] = 1
            return True
        
        if self.goodNodesGivenTarget(root.left, target, arr, visitedNodeList) or self.goodNodesGivenTarget(root.right, target, arr, visitedNodeList):
            return True
        
        arr.pop(-1)
        return False
        
        
