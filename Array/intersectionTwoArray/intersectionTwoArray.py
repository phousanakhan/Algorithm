class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        finalList = []
        longList = []
        shortList = []
        
        if len(nums1) >= len(nums2):
            longList = nums1
            shortList = nums2
        else:
            longList = nums2
            shortList = nums1
    
        
        for value in shortList:
            if value in longList:
                finalList.append(value)
                longList.remove(value)
        
        return(finalList)