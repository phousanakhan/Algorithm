'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.local_area = 0
        self.max_area = 0
        '''
        --psuedo--
        def maxAreaOfIsland
        for value in grid:
            if value = 1:
                dfs(grid, value) and turn 1's --> 0's
        return max #turn              
        '''
        def dfs(idx0, idx1, grid):
            if idx0 < 0 or idx0 >= len(grid) or idx1 < 0 or idx1 >= len(grid[0]) or grid[idx0][idx1] == 0:
                return None

            grid[idx0][idx1] = 0
            self.local_area += 1
            dfs(idx0, idx1-1, grid)
            dfs(idx0, idx1+1, grid)
            dfs(idx0-1, idx1, grid)
            dfs(idx0+1, idx1, grid)
            
        for idx0,row in enumerate(grid):
            for idx1,value in enumerate(row):
                if value == 1:
                    self.local_area = 0
                    dfs(idx0, idx1, grid)
                    self.max_area = max(self.max_area, self.local_area)
        return self.max_area
