class Solution:
    def climbStairs(self, n: int) -> int:
        dict1 = {}
        def fib(n):
            if n <= 2:
                return n
            if n in dict1:
                return dict1[n]
            else:
                dict1[n] = fib(n-1) + fib(n-2)
                return fib(n-1) + fib(n-2)
        return fib(n)