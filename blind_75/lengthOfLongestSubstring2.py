class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        brute force 
        
        longest = 0
        for i in range(len(s)):
            someDict = {s[i]:None}
            for j in range(i+1, len(s)):
                if s[j] not in someDict:
                    #unique
                    someDict[s[j]] = None
                else:
                    break
            longest = max(len(someDict), longest)
        return longest
        '''
        

        '''
        O(n) solution
        
        1. keep track of 2 pointers (front & back) ==> front...back
        2. if front is the same as back, remove front, increment back
        '''
        
        front = 0
        back = 0
        maxLen = 0
        hashMap = {}
        while back < len(s):
            if s[back] not in hashMap:
                hashMap[s[back]] = None
                back += 1
                maxLen = max(back-front, maxLen)
            else:
                del hashMap[s[front]]
                front += 1
        return maxLen
