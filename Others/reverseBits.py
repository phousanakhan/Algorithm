class Solution:
    def reverseBits(self, n: int) -> int:
        #return int(bin(n)[2:].zfill(32)[::-1], 2)
            
        temp = bin(n).replace("0b", "") ##0bxxxxxx. Convert to decimal and remove 0b
        temp = temp.zfill(32) ##add 32 zeroes at the beggining --> 32bits
        temp = temp[::-1] ##reverse the string
        temp = int(temp, 2) ##convert back to binary
        return temp 

