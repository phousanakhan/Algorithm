class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [x1,x2,x3,...,xn]
        *You may assume that each input would have exactly one solution
        
        Thus, there exist some xa & xb s.t.
        xa + xb = target
        
        => xa = target - xb
        
        '''
        hashSet = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in hashSet:
                return [hashSet[diff], index]
            else:
                hashSet[value] = index
