class Solution:
    def longestPalindrome(self, s: str) -> str:
        #abba --> even --> mid + 1
        #aba --> od --> mid
        
        if len(s) < 2:
            return s
        
        #if palindrome itself is odd (remember; not s is odd)
        longest_palindrome_str = ""
        longest_palindrome_len = 0
        for mid in range(0, len(s)):
            for j in range(0, len(s)): #not range(1, len(s)) because we consider a character by itself as a palindrome. E.g, "ab" --> "a"
                left = mid - j
                right = mid + j
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    break
                #print(mid, left, right)
                #e.g, s="qweabaiou" --> aba --> 3..5 --> 5-3+1 = 3
                cur_length = right - left + 1
                if cur_length > longest_palindrome_len:
                    longest_palindrome_len = cur_length
                    longest_palindrome_str = s[left: right+1]
                    
        #if palindrome itself is even (remember; not s is even)
        for mid in range(0, len(s)):
            for j in range(1, len(s)):
                left = mid - j + 1 #abba --> b mid b
                right = mid + j 
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    break
                cur_length = right - left + 1
                if cur_length > longest_palindrome_len:
                    longest_palindrome_len = cur_length
                    longest_palindrome_str = s[left: right+1]
                    
        return longest_palindrome_str
                
        
                
                    
                
        
