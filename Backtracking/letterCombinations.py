class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict0 = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        result = []
        if not digits:
            return result
        else:
            result = ['']
        
        if len(digits) == 1:
            return dict0[digits]
        
        for numb in digits:
            currentCombo = []
            for letter in dict0[numb]:
                for cur_result in result:
                    currentCombo.append(cur_result + letter)
            result = currentCombo
        return(result)
