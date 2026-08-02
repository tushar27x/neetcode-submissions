class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for nei in graph[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order) == numCourses else []