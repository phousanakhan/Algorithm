class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        -intuition for O(m+n) space-
        Iterate through the matrix:
            if that row or col contains 0:
                itself = 0
        '''
        #bool_col = [False] * len(matrix[0])
        width = len(matrix[0])
        height = len(matrix)
        first_row_set_to_zero = False
        for i in range(width):
            if matrix[0][i] == 0:
                first_row_set_to_zero = True
                    
        for i in range(height):
            for m in range(width):
                if matrix[i][m] == 0:
                    matrix[0][m] = 0 #denotes whole column in 0's
                    
        for i in range(1, height):
            row_contains_zero = False
            for j in range(width):
                if matrix[i][j] == 0:
                    row_contains_zero = True
                    break
                    
            for m in range(width):
                if row_contains_zero == True or matrix[0][m] == 0:
                    matrix[i][m] = 0
                    
                    
        if first_row_set_to_zero == True:
            for i in range(width):
                matrix[0][i] = 0

                    
        

                
                    
        
