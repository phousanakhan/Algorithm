import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        alphaStringList = string.ascii_uppercase
        dict0 = {}
        for index, alpha in enumerate(alphaStringList):
            dict0[alpha] = index + 1
        
        total = 0
        for index, value in enumerate(s[::-1]):
            total += dict0[value] * pow(26, index)
            
        return total
