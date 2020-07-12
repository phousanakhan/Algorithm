class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict0 = {}
        dict1 = {}
        
        for index,char in enumerate(s):
            if char in dict0:
                dict0[char] += 1
            else:
                dict0[char] = 1
                dict1[char] = index
                
        for letter in dict0:
            if dict0[letter] == 1:
                return(dict1[letter])
        return(-1)
