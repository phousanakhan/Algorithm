class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
	O(n^3) time
	O(mn) space
        """
        original_matrix = [0] * len(matrix)
        for index,row in enumerate(matrix):
            original_matrix[index] = row[:]
        
        #loop through original; if found 0; modify matrix
        for i in range(0, len(original_matrix)):
            for j in range(0, len(original_matrix[i])):
                if original_matrix[i][j] == 0:
                    self.modifyRow(i, matrix)
                    self.modifyCol(i, j, matrix)
        
    def modifyRow(self, row_index, matrix):
        for col_index,value in enumerate(matrix[row_index]):
            matrix[row_index][col_index] = 0

    def modifyCol(self, row_index, col_index, matrix):
        for index,value in enumerate(matrix):
            matrix[index][col_index] = 0


    
                    
                
                
        
        
