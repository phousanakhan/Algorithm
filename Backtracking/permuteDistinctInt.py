class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finalList = []

        def helper(List: list, startingIndex: int, endingIndex: int):
            if startingIndex == endingIndex:
                tempList = []
                for value in List:
                    tempList.append(value)
                finalList.append(tempList)
                    

            else:
                for i in range(startingIndex, endingIndex+1):
                    List[startingIndex], List[i] = List[i], List[startingIndex] #swap
                    helper(List, startingIndex+1, endingIndex) #recurse
                    List[startingIndex], List[i] = List[i], List[startingIndex] #swap back
                    
            
        helper(nums, 0, len(nums)-1)
        return finalList
