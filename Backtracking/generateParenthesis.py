class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finalList = []
        str = "" * 2 * n
        
        def helper(s: str, countOpening: int, countClosing: int, n: int):
            if countOpening == n and countClosing == n:
                finalList.append(s)
                return

            if countOpening > countClosing:
                helper(s+")", countOpening, countClosing+1, n)

            if countOpening < n:
                helper(s+"(", countOpening+1, countClosing, n)
                
        helper(str, 0, 0, n)
        return finalList
