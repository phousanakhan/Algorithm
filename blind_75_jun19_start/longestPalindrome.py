class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        ***CASE #1: ODD STRING S***
        1. for every element i, assume mid = i, expand i-1, i+1 consecutively
        2. if i-1 == i+1; continue; else, break
        
        
        *** CASE #2: ODD STRING S***
        '''
        max_palindrome = ""
        #**ODD**
        for mid in range(0, len(s)):
            for expand in range(0, len(s)):
                left = mid - expand
                right = mid + expand
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    # print(left,right, s[left:right+1])
                    cur_palindrome = s[left:right+1]
                    if len(cur_palindrome) > len(max_palindrome):
                        max_palindrome = s[left:right+1]
                else:
                    break                  
        #**EVEN**
        for mid in range(0, len(s)):
            for expand in range(1, len(s)):
                left = mid - expand
                right = mid + expand - 1
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_palindrome = s[left:right+1]
                    if len(cur_palindrome) > len(max_palindrome):
                        max_palindrome = s[left:right+1]
                else:
                    break
        return max_palindrome
