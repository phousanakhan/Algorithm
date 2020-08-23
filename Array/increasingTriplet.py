class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool: 
        if len(nums) < 3:
            return False
        firstSmallest = float("inf")
        secondSmallest = float("inf")
        
        for num in nums:
            if num <= firstSmallest: #find firstSmallest
                firstSmallest = num
            elif num <= secondSmallest: #find secondSmallest
                secondSmallest = num
            else: #num is not smaller than secondSmallest and num is not smaller than firstSmallest
                return True
            
            #if exited loop, this means that subsequence of length 3 doesn't exist.
            
        return False
