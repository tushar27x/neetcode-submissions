class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 
        
        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        visited_set = set()

        def dfs(node, parent):
            visited_set.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei in visited_set:
                    return False
                
                if not dfs(nei, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited_set) == n

