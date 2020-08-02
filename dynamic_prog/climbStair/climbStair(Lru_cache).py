from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == None:
            return None
        else:
            return self.fib(n)
        
    @lru_cache(maxsize = 1000)
    def fib(self, n):
        if n <= 2:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)