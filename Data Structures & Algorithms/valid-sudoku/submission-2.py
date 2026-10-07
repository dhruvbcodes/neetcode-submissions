class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(len(board)):
            temp = set()
            for c in range(len(board[0])):
                if board[r][c] != '.' and board[r][c] in temp:
                    return False
                temp.add(board[r][c])

        for c in range(len(board[0])):
            temp = set()
            for r in range(len(board)):
                if board[r][c] != '.' and board[r][c] in temp:
                    return False
                temp.add(board[r][c])

        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                temp = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != '.' and board[i][j] in temp:
                            return False
                        temp.add(board[i][j])

        return True