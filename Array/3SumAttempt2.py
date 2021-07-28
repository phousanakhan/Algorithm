class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        tempArr = []
        nums = sorted(nums)
        for index,value in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]: #no duplicates
                continue
            twoSumArr = self.twoSum(nums[index+1:], -value)
            if len(twoSumArr) == 0:
                continue
            else:
                for arr in twoSumArr:
                    tempArr.append(arr + [value])
        
        finalArr = []
        for arr in tempArr:
            if arr not in finalArr:
                finalArr.append(arr)
        return finalArr
                
    def twoSum(self, nums: List[int], target) -> List[int]:
        valDict = {}
        ret = []
        for index,value in enumerate(nums):
            diff = target - value
            if diff in valDict:
                ret.append([diff, value])
            else:
                valDict[value] = value
        return ret
