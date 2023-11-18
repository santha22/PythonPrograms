class Solution:
    
        
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        ls = []
        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            
            ls.append(root)
            
            inorder(root.right)
            
        inorder(root)
        
        if not ls:
            return None
            
        head = ls[0]
        prev = None
        
        for it in ls:
            if prev:
                prev.right = it
                
            it.left = prev
            prev = it
            
        prev.right = head
        head.left = prev
        
        return head
