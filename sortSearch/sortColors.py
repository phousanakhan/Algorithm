class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0 : red
        1 : white
        2 : blue
        """
        listRed = []
        listWhite = []
        listBlue = []
        
        for i in nums:
            if i == 0:
                listRed.append(i)
            elif i == 1:
                listWhite.append(i)
            else:
                listBlue.append(i)
        nums[:] = []
        nums.extend(listRed + listWhite + listBlue)
        return nums
