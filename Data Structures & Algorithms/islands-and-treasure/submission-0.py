class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        TREASURE = 0
        WATER = -1
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                for i,j in ([(1,0), (-1, 0), (0, 1), (0, -1)]):
                    nr, nc = r + i, c + j
                    if (0<= nr < rows and 0<= nc < cols and (nr, nc) not in visited and grid[nr][nc] != WATER):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                
            dist += 1

                