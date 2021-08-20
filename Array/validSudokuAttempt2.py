class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            print(i)
        isValidRow = self.isValidRow(board)
        isValidCol = self.isValidCol(board)
        isValid3x3 = self.isValid3x3(board)
        #print(isValidRow, isValidCol, isValid3x3)
        return isValidRow == isValidCol == isValid3x3 == True
        
    def isValidRow(self, board):
        for i in range(0, len(board)):
            seenInCurRow = {}
            for j in range(0, len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenInCurRow:
                    return False
                seenInCurRow[board[i][j]] = 1
        return True
    
    def isValidCol(self, board):
        for i in range(0, len(board[0])):
            seenInCurCol = {}
            for j in range(0, len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seenInCurCol:
                    return False
                seenInCurCol[board[j][i]] = 1
        return True
        
    def isUniqueGrid(self, board):
        seenSoFar = {}
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenSoFar:
                    return False
                seenSoFar[board[i][j]] = 1
        return True
    
    def isValid3x3(self, board):
        for i in range(0, len(board), 3):
            board_1 = []
            board_2 = []
            board_3 = []
            for j in range(len(board[i: i+3])):
                board_1.append(board[i: i+3][j][0: 3])
                board_2.append(board[i: i+3][j][3: 6])
                board_3.append(board[i: i+3][j][6: 9])
                
            if self.isUniqueGrid(board_1) == self.isUniqueGrid(board_2) == self.isUniqueGrid(board_3) == True:
                continue
            else:
                return False
            
        return True
            
            
        
