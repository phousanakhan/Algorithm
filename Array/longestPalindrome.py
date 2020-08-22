class Solution:
    def longestPalindrome(self, s: str) -> str:   
        def expandFromMiddle(s: str, left: int, right: int):
            if s == None or left > right: 
                return 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        
            return right - left - 1

        if len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = expandFromMiddle(s, i, i)
            len2 = expandFromMiddle(s, i, i+1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - ((maxLen-1)//2)
                end = i + ((maxLen)//2)
        return s[start: end+1]
