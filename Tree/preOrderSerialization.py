class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        '''
        Intially 1 slot of root 
        Every non-null occupy 1 slot and create 2 --> -1 + 2 = +1
        Every null occupy 1 slot --> -1
        
        Cleanest solution: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)
        '''
        preorder = preorder.split(",")
        slot = 1
        for node in preorder:
            if slot == 0:
                return False
            if node == "#":
                slot -= 1
            else:
                slot += 1
        return slot == 0
