class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums, subset, i):
            if i == len(nums):
                #print(subset)
                tempList = []
                for j in subset:
                    if j != None:
                        tempList.append(j)
                finalList.append(tempList)
                
            else:
                subset[i] = None
                helper(nums, subset, i+1)
                subset[i] = nums[i]
                helper(nums, subset, i+1)
        
        finalList = []
        subset = [None] * len(nums)
        helper(nums, subset, 0)
        return(finalList)
