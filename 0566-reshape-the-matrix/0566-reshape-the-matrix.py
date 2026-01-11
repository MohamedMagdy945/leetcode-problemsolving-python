from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        flat = [val for row in mat for val in row]
        new_mat = []
        for i in range(r):
            new_row = flat[i*c : (i+1)*c] 
            new_mat.append(new_row)
        
        return new_mat
