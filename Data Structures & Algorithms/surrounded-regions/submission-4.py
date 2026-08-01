class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def mark_safe(r,c):
            stk = [(r,c)]
            while stk:
                r,c, = stk.pop()
                if 0<=r<rows and 0<=c<cols and board[r][c] == 'O':
                    board[r][c] = 'S'
                    stk.extend([(r+1,c), (r-1,c), (r,c+1), (r, c-1)])
                
            
        for r in range(rows):
            mark_safe(r,0)
            mark_safe(r, cols-1)
        
        for c in range(cols):
            mark_safe(0, c)
            mark_safe(rows-1, c)
        

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
    