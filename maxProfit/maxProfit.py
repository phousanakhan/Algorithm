class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        listToAdd = []
        returnVal = 0
        for index, value in enumerate(prices):
            try:
                startPoint = prices[1+index]
            except:
                listToAdd.append(0)
                break
            listToAdd.append(int(startPoint - prices[index]))
        
        for i in listToAdd:
            if i >= 0:
                returnVal += i
        return(returnVal)