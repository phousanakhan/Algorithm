class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list0 = []
        for i in range(m):
            list0.append([])
            for j in range(n):
                if i == 0:
                    list0[i].append(1)
                elif j == 0:
                    list0[i].append(1)
                else:
                    list0[i].append(0)
                    
        for i in range(1, m):
            for j in range(1, n):
                list0[i][j] = list0[i-1][j] + list0[i][j-1]  #current = above + left
    
        return list0[-1][-1]
