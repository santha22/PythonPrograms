from collections import deque

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        res = []
        
        if root is None:
            return res
            
        queue = deque()
        queue.append(root)
        leftToRight = True
        
        while queue:
            size = len(queue)
            row = [0] * size
            for i in range(size):
                node = queue.popleft()
                
                index = i if leftToRight else size - 1 - i
                
                row[index] = node.data
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            leftToRight = not leftToRight
            res.extend(row)
            
        return res
