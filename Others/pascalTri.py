class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows == 0:
            return triangle
        
        triangle.append([1])
        for i in range(1, numRows):
            prevRow = triangle[i-1]
            newRow = []
            newRow.append(1)
            
            for j in range(1, len(prevRow)):
                newRow.append(prevRow[j-1] + prevRow[j])
            
            newRow.append(1)
            triangle.append(newRow)
            
        return triangle
