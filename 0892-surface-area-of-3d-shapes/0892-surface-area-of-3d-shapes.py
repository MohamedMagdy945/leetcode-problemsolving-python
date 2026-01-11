class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:

                    total += 2

                    if i == n - 1:
                        total += grid[i][j]
                    else:
                        dif = grid[i][j] - grid[i + 1][j]
                        if dif > 0:
                            total += dif

                    if i == 0:
                        total += grid[i][j]
                    else:
                        dif = grid[i][j] - grid[i - 1][j]
                        if dif > 0:
                            total += dif
                    if j == n - 1:
                        total += grid[i][j]
                    else:
                        dif = grid[i][j] - grid[i][j + 1]
                        if dif > 0:
                            total += dif

                    if j == 0:
                        total += grid[i][j]
                    else:
                        dif = grid[i][j] - grid[i][j -1]
                        if dif > 0:
                            total += dif
        return total
