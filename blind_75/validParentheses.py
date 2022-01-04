class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        l_open = []

        opens = ["(", "{", "["]
        closes = {")":"(", "}": "{", "]": "["}


        for index,value in enumerate(s):
            try:
                if value in opens:
                    l_open.append(value)
                elif len(l_open) > 0 and value in closes and closes[value] == l_open[-1]:
                    del l_open[-1]
                else:
                    return False
            except:
                return False
        return len(l_open) == 0
            
