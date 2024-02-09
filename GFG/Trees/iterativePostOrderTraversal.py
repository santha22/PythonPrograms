class Solution:
    # Return a list containing the inorder traversal of the given tree
    def postOrder(self,node):
        # code here
        preorder = []
        
        if node is None:
            return preorder
            
        stack1, stack2 = [], []
        
        stack1.append(node)
        
        while stack1:
            root = stack1.pop()
            stack2.append(root)
            
            if root.left:
                stack1.append(root.left)
                
            if root.right:
                stack1.append(root.right)
                
        while stack2:
            node = stack2.pop()
            preorder.append(node.data)
            
        return preorder
