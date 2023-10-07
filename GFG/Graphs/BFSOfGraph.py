from collections import deque
class Solution:
    def bfsOfGraph(self,v, adj):
        visited = [0]*v
        q = deque()
        q.append(0)
        bfs = []

        while q:
            node = q.popleft()
            bfs.append(node)
            for item in adj[node]:
                if(visited[item]==0):
                    visited[item]=1
                    q.append(item)
        return bfs


if __name__ == "__main__":
    t = int(input())
    for t in range(t):
        V,E = map(int, input().split())
        adj = [[] for i in range(V)]
        for j in range(E):
            u, v = map(int,input().split())
            adj[u].append(v)

        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end= " ")
        print()
