class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_palindrome = ""
        
        #case 1 - odd substr - 1,3,5,..
        for mid in range(0, len(s)):
            for dist_from_mid in range(0, len(s)):
                left = mid - dist_from_mid
                right = mid + dist_from_mid
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    substr_length = right - left + 1
                    if substr_length > len(longest_palindrome):
                        longest_palindrome = s[left: right+1]
                else:
                    break
                    
        #case 2 - even substr - 1,3,5,..
        for mid in range(0, len(s)):
            for dist_from_mid in range(1, len(s)):
                left = mid - dist_from_mid
                right = mid + dist_from_mid - 1
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    substr_length = right - left + 1
                    if substr_length > len(longest_palindrome):
                        longest_palindrome = s[left: right+1]
                else:
                    break
                    
        return longest_palindrome
        
        
        
