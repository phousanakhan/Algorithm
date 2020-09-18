class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            if matrix:
                row = len(matrix)-1
                col = 0
                width = len(matrix[0])
                while row>=0 and col<width:
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] > target:
                        row -= 1
                    else:
                        col += 1
            return False
        except:
            return False
