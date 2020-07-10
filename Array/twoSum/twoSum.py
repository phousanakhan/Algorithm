class Solution:
    def twoSum(self, nums, target):
        dict0 = {}
        for index,num in enumerate(nums):
            if target-num in dict0:
                return([index, dict0[target-num]])
            else:
                dict0[num] = index

def main():
    _solution = Solution()
    finalList = _solution.twoSum([2,7,11,15], 9)
    print(finalList)
    
if __name__ == "__main__":
    main()