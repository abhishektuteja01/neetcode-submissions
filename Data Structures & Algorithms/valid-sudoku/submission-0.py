class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        for r in range(0,9):
            for i in range(0,9):
                if board[r][i] == '.':
                    continue
                if board[r][i] in row[r]:
                    return False
                row[r].add(board[r][i])
        column = defaultdict(set)
        for c in range(0,9):
            for i in range(0,9):
                if board[i][c] == '.':
                    continue
                if board[i][c] in column[c]:
                    return False
                column[c].add(board[i][c])
        squares = defaultdict(set)
        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in squares[(r//3,c//3)]:
                    return False
                squares[(r//3,c//3)].add(board[r][c])
        return True
                
        