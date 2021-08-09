class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #546 --> 5*10^2  +  4*10^1  +  6*10^0
        num1_int = self.toInt(num1)
        num2_int = self.toInt(num2)
        intBackToString = self.toString(num1_int+num2_int)
        return intBackToString
        
    def toInt(self, num):
        total = 0
        for index,char in enumerate(num[::-1]):
            charToInt = ord(char) - ord('0')
            temp = charToInt * 10 ** index
            total += temp
        return total
    
    def toString(self, num):
        strRet = ""
        '''
        1. int div 10
        2. chr(ord(0) + remainder)
        3. i == 0: break
        '''
        while True:
            num, remainder = divmod(num, 10)
            strRet = chr(ord('0') + remainder)  + strRet
            if num == 0:
                break
        print(type(strRet))
        return strRet
        
            
        
