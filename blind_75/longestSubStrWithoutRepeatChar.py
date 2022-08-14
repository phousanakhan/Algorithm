class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left = 0
        right = 0
        
        hashMap = {}
        maxLen = 0
        while right < len(s):
            if s[right] not in hashMap:
                hashMap[s[right]] = None
                right += 1
            else:
                del hashMap[s[left]]
                left += 1
            maxLen = max(len(hashMap), maxLen)
        return maxLen
                
            
        
