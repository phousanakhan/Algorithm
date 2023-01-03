class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        --intuition--

        Keep track of front & back pointer in a hashMap.
        If back == front, remove front from hashMap.
        Return length of hashMap
        '''
        start = 0
        end = 0
        longest = 0
        hashMap = {}

        while end < len(s):
            if s[end] not in hashMap:
                hashMap[s[end]] = None
                end += 1
                longest = max(longest, len(hashMap))
            else: #s[end] in hashMap
                del hashMap[s[front]] #cant delete s[back] else we never increment the front so it will always stuck at p for pwwkew etc
                front += 1
        return longest
