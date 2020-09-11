class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict0 = {}
        for index,value in enumerate(nums):
            if value in dict0:
                dict0[value].append(1)
            else:
                dict0[value] = [1]
                
        finalList = []
        for index,m in enumerate(sorted(dict0, key=lambda m: len(dict0[m]), reverse=True)):
            if index >= k:
                break
            finalList.append(m)
        
        return(finalList)
