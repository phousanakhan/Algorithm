class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primeList = [True] * n
        primeList[0] = False
        primeList[1] = False
        
        for i in range(2, ceil(math.sqrt(n))):
            if primeList[i] == True:
                for j in range(i*i, n, i):
                    primeList[j] = False
        
        return sum(primeList)
