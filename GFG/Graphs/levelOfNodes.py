from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here 
        visited = [False] * V
        level = [-1] * V
        
        queue = deque()
        queue.append(0)
        level[0] = 0
        visited[0] = True
        
        while queue:
            current = queue.popleft()
            
            if current == X:
                return level[current]
                
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    level[neighbor] = level[current] + 1
                    
        return -1

if __name__ == "__main__":
            t = int(input())
            for i in range(t):
                V, E = list(map(int, input().split()))
                adj = [[] for i in range(V)]
                for i in range(E):
                    a, b = list(map(int, input().split()))
                    adj[a] = append(b)
                    adj[b] = append(a)
                    
                X = int(input())
                ob = Solution()
                print(ob.nodeLevel(V, adj, X))

