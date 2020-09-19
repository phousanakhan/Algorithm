class Solution:
    def canJump(self, nums: List[int]) -> bool:
        MaxReach = 0
        i = 0
        while i < len(nums) and i <= MaxReach:
            MaxReach = max(MaxReach, i+nums[i])
            i += 1
        return i == len(nums)

