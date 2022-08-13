

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        ans_set = set()
        for index,target in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]: #skip duplicate
                continue
            #a+b+c=0 ==> a+b = -c
            self.twoSum(nums[index+1: ], -target, ans_set)
        ret = [list(x) for x in ans_set]
        return ret
        
        
        
    def twoSum(self, nums, target, ans_set):
        d = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in d:
                ans_set.add((diff, value, -target))
            else:
                d[value] = index
