class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, path= [], []

        def is_valid(row, col):
            for prev_row in range(row):
                prev_col = path[prev_row]
                if prev_col == col:
                    return False
                if abs(prev_row - row) == abs(prev_col - col):
                    return False
            
            return True
            
        def backtrack(row):
            if row == n:
                board = []
                for c in path:
                    line = "."*c +'Q'+'.'* (n-c-1)
                    board.append(line)

                res.append(board)

            for col in range(n):
                if not is_valid(row, col):
                    continue
                
                path.append(col)
                backtrack(row+1)
                path.pop()

        backtrack(0)
        return res