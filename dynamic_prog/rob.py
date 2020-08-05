class Solution:
    def rob(self, nums: List[int]) -> int:
        try:
            if len(nums) <= 2:
                return(max(nums))

            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = prev1
                prev1 = max(prev1, nums[i]+prev2)
                prev2 = temp
            return(prev1)
        except:
            return 0