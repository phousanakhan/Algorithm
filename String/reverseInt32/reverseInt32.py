class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return(0)  
        
        list1 = []      
        for num in str(x):
            if num.isdigit():
                list1.append(num)
        list1.reverse()
        
        if list1[-1] == "0":
            list1.remove(list1[-1])

        if str(x)[0] == "+" or str(x)[0] == "-":
            list1.insert(0,(str(x)[0]))
            
            
        modNum = int(''.join(list1))
        lowerLimit = -0x80000000
        upperLimit = 0x7fffffff
        if modNum < 0:
            val = lowerLimit & modNum
            if val == lowerLimit:
                return(modNum)
            else:
                return(0)
        if modNum > 0:
            val = upperLimit & modNum
            if val == modNum:
                return(modNum)
            else:
                return(0)