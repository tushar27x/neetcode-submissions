class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        visited_set = set()
        count = 0

        def dfs(node):
            visited_set.add(node)
            for nei in graph[node]:
                if nei not in visited_set:
                    dfs(nei)
            
        for node in range(n):
            if node not in visited_set:
                dfs(node)
                count += 1
        
        return count
        


        
