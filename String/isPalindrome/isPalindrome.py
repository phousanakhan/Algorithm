import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        listForward = []
        listBackward = []
    
        for char in s:
            if char.isalnum():
                listForward.append(char)
        strForward = "".join(listForward)
        if strForward.lower() == strForward[::-1].lower():
            return(True)
        else:
            return(False)