class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd_case = self.potentialPalindrome(s, 0)
        even_case = self.potentialPalindrome(s, 1)
        if len(odd_case) > len(even_case):
            return odd_case
        else:
            return even_case
        
        
    def potentialPalindrome(self, s, offset):
        curPal = ""
        for mid_idx in range(0, len(s)):
            for dist_from_mid_idx in range(offset, len(s)):
                left = mid_idx - dist_from_mid_idx
                right = mid_idx + dist_from_mid_idx - offset
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    if len(s[left:right+1]) > len(curPal):
                        curPal = s[left:right+1]
                else:
                    break
        return curPal
