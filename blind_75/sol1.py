class Solution:
    def longestPalindrome(self, s: str) -> str:
        #if palindrome length is odd
        longest = ""
        for index_mid, mid in enumerate(s):
            for index_offset in range(0, len(s)):
                left = index_mid - index_offset
                right = index_mid + index_offset
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    # print(s[left], mid, s[right], right - left + 1)
                    curLen = right - left + 1
                    if curLen > len(longest):
                        longest = s[left: right + 1]
                else:
                    break
        
        #if palindrome length is even
        
        #we do len(s)-1 because this denotes that actual mid is between mid, mid+1 ==> mid, actual_mid, mid+1
        #example ==> abba; if mid is a|b|ba (b); the actual_mid is ab||ba (so between mid (first b) and mid+1 (second b))
        for index_mid in range(0, len(s)-1):
            for index_offset in range(1, len(s)):
                #+1 because we want actual mid to between in between mid, mid + 1
                #so 1. index_offset=1; then this give char x s.t. mid, x, mid + 1
                #   2. index_offset=2; then this give char x s.t. mid+1, x, mid + 2
                left = index_mid - index_offset + 1
                right = index_mid + index_offset
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    # print(s[left], mid, s[right], right - left + 1)
                    curLen = right - left
                    if curLen > len(longest):
                        longest = s[left: right + 1]
                else:
                    break
        return longest
