class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        totalArea = 0
        n = len(grid)
        for i in range(n):
            maxRow = 0
            for j in  range(n):
                if grid[i][j] > 0 :
                    totalArea += 1
                if grid[i][j] > maxRow :
                    maxRow = grid[i][j]
            totalArea += maxRow

        for i in range(n):
            maxColumn = 0
            for j in range(n):
                if grid[j][i] > maxColumn:
                    maxColumn = grid[j][i]
            totalArea += maxColumn
        return  totalArea