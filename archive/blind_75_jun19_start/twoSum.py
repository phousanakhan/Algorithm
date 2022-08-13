class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        --Intuition--
        
        1. For every number in an array of numbers, we can calculate diff = target - numbers[i]
        2. We then then check if diff is in a dictionary, if it is, return.
        3. If not, we store the numbers[i] in the dictionary
        
        '''
        
        hash_map = {}
        for index,number in enumerate(nums):
            diff = target - number
            if diff in hash_map:
                return [hash_map[diff], index]
            else:
                hash_map[number] = index
