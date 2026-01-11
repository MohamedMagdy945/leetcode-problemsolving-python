class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 1
        j = 1
        while i < len(matrix):
            while j < len(matrix[i]):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
                j += 1
            i += 1
            j = 1
        return True
