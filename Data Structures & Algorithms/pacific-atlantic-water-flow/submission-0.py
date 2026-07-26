class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        rows, cols = len(heights), len(heights[0])
        
        def bfs(start, visited):
            q = deque(start)
            visited.update(start)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for i,j in directions:
                        nr, nc = r+i, c+j
                        if(0<=nr<rows and 0<=nc<cols and
                            heights[nr][nc] >= heights[r][c] and 
                            (nr,nc) not in visited
                        ):
                            q.append((nr,nc))
                            visited.add((nr,nc))
        


        pacific_start = [(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]
        atlantic_start = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        bfs(pacific_start, pacific_set)
        bfs(atlantic_start, atlantic_set)

        return [[r,c] for r in range(rows) for c in range(cols) if (r,c) in pacific_set and (r,c) in atlantic_set]