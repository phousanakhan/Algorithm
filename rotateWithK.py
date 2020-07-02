class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
