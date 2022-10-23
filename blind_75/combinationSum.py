class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        finalList = []
        def recurse(candidates, target, tempList, start):
            if target == 0:
                finalList.append(tempList[:])
            elif target < 0:
                return 
            else:
                for index in range(start, len(candidates)):
                    tempList.append(candidates[index])
                    recurse(candidates, target-candidates[index], tempList, index)
                    del tempList[len(tempList)-1]

        recurse(candidates, target, [], 0)
        return finalList
