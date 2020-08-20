class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Get Position of 0's
        listTup = []
        for index0, list0 in enumerate(matrix):
            for index1,value1 in enumerate(list0):
                if value1 == 0:
                    listTup.append((index0,index1))
        
        
        for tup in listTup:
            print(tup)
            for row in range(0, len(matrix)):
                matrix[row][tup[1]] = 0 #change all column -> 0. Must iterate row
            for col in range(0, len(matrix[0][:])): #change all row -> 0. Must iterate col
                matrix[tup[0]][col] = 0
