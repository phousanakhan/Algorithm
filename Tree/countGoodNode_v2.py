# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #--intuition--
        '''
        Iterate through the tree and keep track of the biggest value seen so far.
        If the biggest value is greater than the current value --> "bad node"
        '''
        biggest_value_seen_so_far = float('-inf')
        self.bad_node = 0
        self.total_node = 0
        def bfs(root, biggest_value_seen_so_far):
            if root == None:
                return 0
            #update biggest value
            if root.val > biggest_value_seen_so_far:
                biggest_value_seen_so_far = root.val

            if root.val < biggest_value_seen_so_far:
                self.bad_node += 1
            bfs(root.left, biggest_value_seen_so_far)
            self.total_node += 1
            bfs(root.right, biggest_value_seen_so_far)
            
        bfs(root, biggest_value_seen_so_far)
        return self.total_node - self.bad_node
