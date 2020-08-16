class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        list1 = []
        dict0 = {"(":")", "{":"}", "[":"]"}
        dict1 = {")":"(", "}":"{", "]":"["}
        for index, paren in enumerate(s):
            if paren in dict0:
                list1.append(paren)
            elif paren in dict1 and len(list1) > 0 and list1[-1] == dict1[paren]:
                del list1[-1]
            else:
                return False
            
        if len(list1) > 0:
            return False
        else:
            return True
