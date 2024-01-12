from collections import deque

#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        # code here
        l = deque()
        
        for i in range(k):
            l.append(q[i])
            
        for i in range(k):
            q[i] = l.pop()
            
        return q
