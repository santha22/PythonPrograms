class Solution:
    def dfs(self, node, adj, visited, parent):
        visited[node] = 1
        for item in adj[node]:
                
            # checking for node is visited or not
            if visited[item] == 0:
                if self.dfs(item, adj, visited, node) == 1:
                    return 1
                    
                
            # checking for loop
            elif item != parent:
                return 1
                
        return 0
    
    
    def isTree(self, n, m, edges):
        # Code here
        adj = [[] for i in range(n)]
        
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
        start = 0
        parent = -1
        visited = [0] * n
        
        if self.dfs(start, adj, visited, parent) == 1:
            return 0
            
        for i in range(n):
            # if not visited then it is not connected
            if visited[i] == 0:
                return 0
                
        return 1
