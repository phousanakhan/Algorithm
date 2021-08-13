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
        bool_col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    bool_col[j] = True
        
        for i in range(len(matrix)):
            row_contains_zero = False
            for m in range(len(matrix[i])):
                if matrix[i][m] == 0:
                    row_contains_zero = True
                    break
                    
            for j in range(len(matrix[i])):
                if row_contains_zero == True or bool_col[j] == True:
                    matrix[i][j] = 0
                    
        

                    
        

                
                    
        
