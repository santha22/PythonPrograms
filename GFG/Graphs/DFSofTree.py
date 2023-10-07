
class Solution:
    def dfs(self,node, visited, adj, dfsList):
        visited[node] = 1
        dfsList.append(node)

        for item in adj[node]:
            if(visited[item]==0):
                self.dfs(item, visited, adj, dfsList)

    def dfsOfGraph(self, v, adj):
        visited = [0]*v
        start = 0
        dfsList = []
        self.dfs(start, visited, adj, dfsList)
        return dfsList


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        V,E  = map(int,input().split())
        adj = [[] for i in range(V)]
        for j in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for j in range(len(ans)):
            print(ans[j], end=" ")
        print()
