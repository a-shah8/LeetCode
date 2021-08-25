## Backtracking - DFS

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(cur_node, path):
            if cur_node == len(graph)-1:
                result.append(path)
            else:
                for link in graph[cur_node]:
                    dfs(link, path+[link])
                    
        result = []
        dfs(0, [0])
        
        return result
