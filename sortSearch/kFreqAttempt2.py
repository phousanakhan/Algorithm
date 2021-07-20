'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictFreq = {}
        for index,num in enumerate(nums):
            if num in dictFreq:
                dictFreq[num] += 1
            else:
                dictFreq[num] = 1
        return list(sorted(dictFreq, key=dictFreq.get, reverse=True)[0: k])
        #return a list of dictionary's key sorted by largest frequency up to k
