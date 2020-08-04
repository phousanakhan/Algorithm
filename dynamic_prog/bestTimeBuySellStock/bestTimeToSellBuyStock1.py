class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or prices == []:
            return 0
        MAX = 0
        MIN = sys.maxsize
        for index,price in enumerate(prices):
            if price < MIN:
                MIN = price
            else:
                MAX = max(MAX, prices[index] - MIN)
        return(MAX)