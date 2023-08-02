class Solution:
    def dfs(self, node, visited, adj, dfsList, parent):
        visited[node] = 1
        dfsList.append(node)
        for item in adj[node]:
            if(visited[item]==0):
                if(self.dfs(item, visited, adj, dfsList, node)==1):
                    return 1
            elif item != parent:
                return 1
        return 0

    def isTree(self, n, adj):
        visited = [0]*n
        start = 0
        parent = -1
        dfsList = []
        if(self.dfs(start, visited, adj, dfsList,parent)==1):
            return False
        for i in range(n):
            if(visited[i]==0):
                return False
        return True

for i in range(int(input())):
    n,m = [int(i) for i in input().split()]
    adj = [[] for i in range(n)]
    for i in range(m):
        u,v = [int(i) for i in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    ob = Solution()
    print(ob.isTree(n,adj))