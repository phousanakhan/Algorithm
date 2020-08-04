class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        try:
            maxGlobal = nums[0]
            maxCurrent = nums[0]
            for i in range(1, len(nums)):
                maxCurrent = max(nums[i], maxCurrent+nums[i])
                maxGlobal = max(maxCurrent, maxGlobal)
            return maxGlobal
        except:
            return None