class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, low, high, target):
            first = nums[0]
            if high >= low:
                mid = (low + high)//2
                if nums[mid] == target:
                    return mid
                
                amBig = (nums[mid] >= first)
                targetBig = (target >= first)
                if amBig == targetBig: #target in before pivot list
                    if nums[mid] < target:
                        return helper(nums, mid+1, high, target)
                    else:
                        return helper(nums, low, mid-1, target)
                else:
                    if amBig:
                        return helper(nums, mid+1, high, target)
                    else:
                        return helper(nums, low, mid-1, target)
            else:
                return -1
            
        return(helper(nums, 0, len(nums)-1, target))
