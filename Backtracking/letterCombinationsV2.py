class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        alphaDict = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
                    }
        
        ans = []
        ansF = []
        return self.helper(digits, alphaDict, 0, ans, ansF)
    
    def helper(self, digits, alphaDict, start, ans, ansF):
        #-- BASE CASE --
        if start == len(digits):
            return ans
        #---------------
        
        if len(ans) == 0:
            for i in list(alphaDict[int(digits[start])]):
                ans.append(i)
        else:
            for index,value in enumerate(ans):
                for j in list(alphaDict[int(digits[start])]):
                    ansF.append(ans[index]+j)
        
            ans = ansF[:]
            ansF.clear()
        
        return self.helper(digits, alphaDict, start+1, ans, ansF)
