class Solution:
    def hammingWeight(self, n: int) -> int:
        #return bin(n).replace("0b", "").count("1")
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

