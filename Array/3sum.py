class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalList = []
        for i in range(0, len(nums) - 2):
            if i == 0 or (i>0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                sumf = 0 - nums[i]
                while(low < high):
                    if nums[low] + nums[high] == sumf:
                        finalList.append([nums[i], nums[low], nums[high]])
                        while ((low < high) and (nums[low] == nums[low+1])):
                            low += 1
                        while ((low < high) and (nums[high] == nums[high-1])):
                            high -= 1
                        low += 1
                        high -= 1
                    elif ((nums[low]+nums[high]) > sumf):
                        high -= 1
                    else:
                        low += 1
        return finalList
