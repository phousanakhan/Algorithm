class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''brute force ==>
        go through each cell; try 1->9; check board; 
        '''
        self.solve(board)
    def solve(self, board):
            counter = 0
            for i in range(0, len(board)):
                for j in range(0, len(board[0])):
                    if board[i][j] == ".":
                        for str_i in "123456789":
                            #check whether adding str_i will be valid
                            if self.value_is_valid(str_i, board, i, j) == True:
                                board[i][j] = str_i
                                if self.solve(board) == True: #if its the solution
                                    return True
                                else:
                                    board[i][j] = "." #go back
                        return False #went through 1->9 and non are solution
            return True
    
    def value_is_valid(self, str_value, board, row, col):
        for i in range(0, 9):
            if board[row][i] != "." and board[row][i] == str_value:
                return False
            if board[i][col] != "." and board[i][col] == str_value:
                return False
            subi = row//3
            subj = col//3
            for p in range(subi*3, (subi+1)*3):
                for q in range(subj*3, (subj+1)*3):
                    if board[p][q] == str_value:
                        return False
        return True

            
                            
