class Solution:
    def myAtoi(self, str: str) -> int:
        finalList = []
        if len(str) == 0:
            return(0)
        
        str = str.strip()
        str = str.rstrip('+')
        str = str.rstrip('-')
        
        count = 0
        for j in range(0,len(str)):
            if (str[j] == '+' or str[j] == '-') and count == 0:
                finalList.append(str[j])
                count += 1

            elif str[j].isdigit() == True:
                finalList.append(str[j])
                
            else:
                break

        try:
            int((''.join(finalList))) + 1
        except:
            return(0)
        
        if (int((''.join(finalList)))) == 0:
            return(0)
        
        if len(finalList) == 0:
            return(0)
     
        else:
            lowerLimit = -0x80000000
            upperLimit = 0x7fffffff
            finalNumb = int((''.join(finalList)))


            if finalNumb < 0:
                val = lowerLimit & finalNumb
                if val == lowerLimit:
                    return(finalNumb)
                else:
                    return(lowerLimit)
            if finalNumb > 0:
                val = upperLimit & finalNumb
                if val == finalNumb:
                    return(finalNumb)
                else:
                    return(upperLimit)