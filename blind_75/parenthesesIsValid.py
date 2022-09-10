class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        hashMap = {")":"(", "}":"{", "]":"["}
        Opens = ["(", "{", "["]
        tList = []
        tInvalid = [] #handle case s.a. ")(){}" where closing is first
        for idx,value in enumerate(s):
            if value in Opens:
                tList.append(value)
                #a closing bracket
            elif len(tList) > 0 and hashMap[value] == tList[-1]:
                del tList[-1]
            else:
                tInvalid.append(value)
        return len(tList) == 0 and len(tInvalid) == 0
