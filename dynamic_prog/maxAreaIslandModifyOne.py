from copy import deepcopy
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        length, allOne = 0, 0
        tempGrid = [0] * len(grid)
        for idx,value in enumerate(grid):
            tempGrid[idx] = grid[idx][:]
        
        globalMax = 0
        for index1, row in enumerate(tempGrid):
            for index2, row in enumerate(row):
                length += 1
                if tempGrid[index1][index2] == 0:
                    tempGrid[index1][index2] = 1
                    globalMax = max(globalMax, self.maxAreaOfIsland(tempGrid))
                    tempGrid = [0] * len(grid)
                    #for idx,value in enumerate(grid):
                        #tempGrid[idx] = grid[idx][:]
                    tempGrid = deepcopy(grid)
                else:
                    allOne += 1
        if length == allOne:
            return allOne
        else:
            return(globalMax)
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:   
        self.maxArea = 0
        self.maxFinal = 0
        def dfs(index0, index1, grid, areaCounter=0):
            if index0 >= len(grid) or index0 < 0 or index1 >= len(grid[0]) or index1 < 0 or grid[index0][index1] == 0:
                #complete flipping
                return None

            #--FLIPPING--
            grid[index0][index1] = 0
            self.maxArea += 1
            #---DFS---
            dfs(index0-1,index1,grid,areaCounter) 
            dfs(index0+1,index1,grid,areaCounter)
            dfs(index0,index1+1,grid,areaCounter)
            dfs(index0,index1-1,grid,areaCounter)
            
        islandCounter = 0
        for index0,row in enumerate(grid):
            for index1,val in enumerate(row):
                if grid[index0][index1] == 1:
                    dfs(index0,index1,grid, 0)
                    islandCounter += 1
                    self.maxFinal = max(self.maxFinal, self.maxArea)
                    self.maxArea = 0
        return self.maxFinal
        class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        for each 0's:
            change 0 --> 1
            get maxCurArea #can have multiple island; so get maxCurArea
            maxArea = max(maxArea, maxCurArea)
        '''

        self.curAreaCounter = 0
        globalMaxArea = 0
        allOne = 0
        totalLength = 0
    
        def getMaxCurArea(index1, index2, grid):
            if index1 < 0 or index1 >= len(grid) or index2 < 0 or index2 >= len(grid[0]) or grid[index1][index2] == 0:
                return
            grid[index1][index2] = 0
            self.curAreaCounter += 1
            getMaxCurArea(index1, index2-1, grid)
            getMaxCurArea(index1, index2+1, grid)
            getMaxCurArea(index1-1, index2, grid)
            getMaxCurArea(index1+1, index2, grid)
            

        for index1, row in enumerate(grid):
            for index2, value in enumerate(row):
                totalLength += 1
                if grid[index1][index2] == 0:
                    grid[index1][index2] = 1
                    getMaxCurArea(index1, index2, grid)
                    grid[index1][index2] = 0
                    globalMaxArea = max(globalMaxArea, self.curAreaCounter)
                    self.curAreaCounter = 0
                else:
                    allOne += 1
        
        
        if totalLength == allOne:
            return allOne
        else:
            return globalMaxArea
        
        
                    
