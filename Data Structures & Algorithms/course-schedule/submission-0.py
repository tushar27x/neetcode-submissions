class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            graph[b].append(a)

        WHITE, GRAY, BLACK = 0,1,2
        state = [WHITE]*numCourses

        def dfs(node):
            if state[node] == GRAY:
                return False
            if state[node] == BLACK:
                return True
            
            state[node] = GRAY
            neighbours = graph[node]
            for n in neighbours:
                if not dfs(n):
                    return False
            
            state[node] = BLACK
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True