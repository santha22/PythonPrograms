class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        q = deque()
        q.append(root)
        
        ls = []
        
        while q:
            node = q.popleft() 
            ls.append(node.data)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        return ls
