class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = sum(nums)
        complete = (len(nums) * (len(nums) + 1)) / 2
        return int(complete - missing)
