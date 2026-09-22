class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        sqrs = [0]*9

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1
                mask = 1 << val
                if mask & rows[i] or mask & cols[j] or mask & sqrs[(i//3)*3 +j//3]:
                    return False
                rows[i] |= mask
                cols[j] |= mask
                sqrs[(i//3)*3 +j//3] |= mask
        return True