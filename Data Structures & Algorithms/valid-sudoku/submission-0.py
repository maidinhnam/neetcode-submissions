class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = range(len(board))

        for l in n:
            lst = [1]*9
            for c in n:
                if board[l][c] != '.':
                    lst[int(board[l][c])-1] -= 1
            for i in range(9):
                if lst[i]<0:
                    return False

        for l in n:
            lst = [1]*9
            for c in n:
                if board[c][l] != '.':
                    lst[int(board[c][l])-1] -= 1
            for i in range(9):
                if lst[i]<0:
                    return False



        for l in range(int(len(n)/3)):
            for c in range(int(len(n)/3)):
                lst = [1]*9
                for x in range(3):
                    for y in range(3):
                        if board[3*l+x][3*c+y] != '.':
                            lst[int(board[3*l+x][3*c+y])-1] -= 1
                for i in range(9):
                    if lst[i]<0:
                        return False
        return True