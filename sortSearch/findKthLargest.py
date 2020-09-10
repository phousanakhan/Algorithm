class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums[:] = sorted(nums)
        nums[:] = nums[::-1]
        print(nums)
        kthLargest = float('inf')
        count = 0
        for i in range(0,len(nums)):
    
            if nums[i] <= kthLargest:
                kthLargest = nums[i]
                count += 1
                
            if count == k:
                return kthLargest
