from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        cellMap = defaultdict(set)

        for r in range(9):
            for c in range(9):
                number = board[r][c]
                if number == ".": continue
                if number in rowMap[r] or number in colMap[c] or number in cellMap[(r//3, c//3)]:
                    return False
                rowMap[r].add(number)
                colMap[c].add(number)
                cellMap[(r//3,c//3)].add(number)
        return True