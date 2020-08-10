class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        start = 1
        while n > start:
            start = start * 3
        
        if start == n:
            return True
        else:
            return False
