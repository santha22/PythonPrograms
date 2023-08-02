# User function Template for python3

class Solution:
    def dfs(self, node, adjLs, visited):
        visited[node] = 1
        for item in adjLs[node]:
            if (visited[item] == 0):
                self.dfs(item, adjLs, visited)

    def numProvinces(self, adj, v):
        # code here

        adjLs = [[] for _ in range(v)]
        for i in range(v):
            for j in range(v):
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)

        visited = [0] * v
        count = 0
        for i in range(v):
            if visited[i] == 0:
                count += 1
                self.dfs(i, adjLs, visited)
        return count


if __name__ == "__main__":
    t = int(input())
    for t in range(t):
        v = int(input())
        adj = []
        for i in range(v):
            temp = list(map(int, input().split()))
            adj.append(temp)
        ob = Solution()
        print(ob.numProvinces(adj,v))