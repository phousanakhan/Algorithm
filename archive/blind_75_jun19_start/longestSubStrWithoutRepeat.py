class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        --intuition--
        ##Sliding window technique##
        
        1. mid,left,right = 0
        2. ith iter 
            ==> increment right+=1. If unique, continue increment right+=1
            if duplicate, increment left up until and including the duplicate element
        
        '''
        
        left, right = 0, 0
        hash_map = {}
        longest = 0
        while right < len(s):
            if s[right] not in hash_map:
                #unique char
                hash_map[s[right]] = 1
                right += 1
            else:
                del hash_map[s[left]]
                left += 1
            longest = max(len(hash_map), longest)
        return longest
