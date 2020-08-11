class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        try:
            total = 0
            for index,letter in enumerate(s):
                if dict1[letter] < dict1[s[index+1]]:
                    total -= dict1[letter]
                else:
                    total += dict1[letter]
        except:
            return total + dict1[s[-1]] 
        
##When index+1 element is out of range, last element is not evaluated. Thus, we add the last element. We can be certain that last element is correct as there's no next element after last element.
