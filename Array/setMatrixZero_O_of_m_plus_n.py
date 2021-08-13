class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        -intuition for O(m+n) space-
        1. Create bool_row; contains T/F whether that row contains 0
	2. Create bool_col; contains T/F whether that col contains 0
	3. Iterate through matrix; 
	4. If matrix[i][j] have T in bool_row or bool_col
		matrix[i][j] = 0
	5.DONE
        '''
        
        #Get bool_list for row
        bool_row = [False] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    bool_row[i] = True
                    break
        
        #Get bool_list for col
        bool_col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j])
                if matrix[i][j] == 0:
                    bool_col[j] = True
                    #break
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if bool_row[i] == True or bool_col[j] == True:
                    matrix[i][j] = 0
        
                
        

                
                    
        
