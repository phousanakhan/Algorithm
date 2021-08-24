class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real0, img1 = num1.split("+")
        real2, img3 = num2.split("+")
        #print(real0, img1)
        #print(real2, img3)
        #p1 + p2 + p3 + p4
        
        p1 = int(real0)*int(real2)
        p2 = int(real0)*int(img3.split("i")[0]) #i
        
        p3 = int(img1.split("i")[0]) * int(real2) #i
        p4 = int(img1.split("i")[0]) * int(img3.split("i")[0]) #i2
        
        f1 = str(p2 + p3) + "i"
        f2 = p4 * -1
        f3 = str(p1 + f2) + "+"
        
        final = str(f3) + f1
        return(final)
