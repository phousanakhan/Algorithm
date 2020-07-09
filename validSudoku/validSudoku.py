class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        B1 = self.checker1(board)
        B2 = self.checker0(board)

            
        if B1 and B2:
            return(True)
        else:
            return(False)

    def checker0(self, board):
        for index, valueRow in enumerate(board):
            print(valueRow)
            for index1,value0 in enumerate(valueRow):
                if value0 != ".":
                    if valueRow.count(value0) > 1:
                        return(False)
        
        list1 = []
        for index, valueRow in enumerate(board):
            list2 = []
            for index1,value0 in enumerate(valueRow):
                if board[index1][index] != ".":
                    list2.append(board[index1][index])
            list1.append(list2)
    
        for index,valueRow in enumerate(list1):
            for index1, value0 in enumerate(valueRow):
                if valueRow.count(value0) > 1:
                    return(False)
        
        return(True)
                    
    def checker1(self, board):
        x = 0
        y = 3
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        
        for i in range(x,y):
            list1.extend([board[i][0:3], board[i+1][0:3], board[i+2][0:3]])
            list2.extend([board[i][3:6], board[i+1][3:6], board[i+2][3:6]])
            list3.extend([board[i][6:9], board[i+1][6:9], board[i+2][6:9]])
            break
        for i in range(x+3,y+3):
            list4.extend([board[i][0:3], board[i+1][0:3], board[i+2][0:3]])
            list5.extend([board[i][3:6], board[i+1][3:6], board[i+2][3:6]])
            list6.extend([board[i][6:9], board[i+1][6:9], board[i+2][6:9]])
            break
            
        for i in range(x+6,y+6):
            list7.extend([board[i][0:3], board[i+1][0:3], board[i+2][0:3]])
            list8.extend([board[i][3:6], board[i+1][3:6], board[i+2][3:6]])
            list9.extend([board[i][6:9], board[i+1][6:9], board[i+2][6:9]])
            break
        print(list2)
        
        
        if (self.threeCheck(list1)) and (self.threeCheck(list2)) and (self.threeCheck(list3)) and                      (self.threeCheck(list4)) and (self.threeCheck(list5)) and (self.threeCheck(list6)) and                      (self.threeCheck(list7)) and (self.threeCheck(list8)) and (self.threeCheck(list9)) == True:
            return(True)
        else:
            return(False)
        
        
        
    def threeCheck(self, board):
        dict0 = {}
        for i in board:
            for j in i:
                if j != ".":
                    if j in dict0:
                        return(False)
                    else:
                        dict0[j] = 1
        return(True)
