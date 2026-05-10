class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        terminal, visited = set(), set()
        def dfs(node):
            print node
            if node not in visited:
                visited.add(node)
                if not graph[node] or all(dfs(i) for i in graph[node]):
                    terminal.add(node)
            return node in terminal
        
        return [i for i,j in enumerate(graph) if dfs(i)]

