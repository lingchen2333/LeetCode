from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols -1
        while l <= r:
            m = (l+r)//2
            row = m//cols
            col = m % cols
            if matrix[row][col] > target:
                r = m-1
            elif target> matrix[row][col]:
                l = m+1
            else: 
                return True
        return False