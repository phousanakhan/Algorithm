class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # FRONT --- BACK
        dict0 = {}
        ptrBack = 0
        ptrFront = 0
        maxList =  []
        while ptrBack < len(s):
            if s[ptrBack] not in dict0:
                dict0[s[ptrBack]] = 1
                ptrBack += 1
                maxList.append(len(dict0))
            else:
                del dict0[s[ptrFront]]
                ptrFront += 1
                
        if maxList == []:
            return len(s)
        else:
            return max(maxList)
