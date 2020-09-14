class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        if len(nums) == 1:
            return 0
        
        largest = float('-inf')
        index0 = float('-inf')
        for index,value in enumerate(nums):
            if value > largest:
                largest = value
                index0 = index
            else:
                break
        return index0
