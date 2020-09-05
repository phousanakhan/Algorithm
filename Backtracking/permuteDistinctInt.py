class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finalList = []

        def helper(List: list, startingIndex: int, endingIndex: int):
            if startingIndex == endingIndex:
                finalList.append(List[:]) 
                #List[:] to make a copy; else, it will be a reference

            else:
                for i in range(startingIndex, endingIndex+1):
                    List[startingIndex], List[i] = List[i], List[startingIndex] #swap
                    helper(List, startingIndex+1, endingIndex) #recurse
                    List[startingIndex], List[i] = List[i], List[startingIndex] #swap back
                    
            
        helper(nums, 0, len(nums)-1)
        return finalList
