class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh > 0:
            time += 1

            for _ in range(len(q)):
                r,c = q.popleft()
                for i,j in directions:
                    nr, nc = r+i, c+j
                    if(0<= nr < rows and
                       0<= nc < cols and
                       grid[nr][nc] == 1
                    ):
                        q.append((nr,nc))
                        fresh -= 1
                        grid[nr][nc] = 2
                
        return time if fresh == 0 else -1


