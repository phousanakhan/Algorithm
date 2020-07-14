class Solution:
    def longestCommonPrefix(self, strs):
        list1 = []
        size = len(strs) 

        # if size is 0, return empty string  
        if (size == 0): 
            return "" 

        if (size == 1): 
            return strs[0] 

        # sort the array of strings  
        strs.sort() 
        print(strs)

        # find the minimum length from  
        # first and last string  
        firstWordLen = len(strs[0])
        lastWordLen = len(strs[-1])
                          
        minLen = min(firstWordLen, lastWordLen)
        #print(minLen)
        
        i = 0
        while i < minLen:
            if strs[0][i] == strs[size-1][i]:
                print(strs[0][i], strs[-1][i])
                list1.extend(strs[0][i])
                i += 1
            else:
                break
        return(''.join(list1))