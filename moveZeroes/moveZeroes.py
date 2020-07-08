class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCounter = nums.count(0)
        #print(zeroCounter)
        while 0 in nums:
            nums.remove(0)
            
        for i in range((zeroCounter)):
            nums.append(0)