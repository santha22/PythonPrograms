class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        # code here
        preorder = []
        if root is None:
            return preorder
            
        s = []
        s.append(root)
        
        while s:
            topNode = s.pop()
            preorder.append(topNode.data)
            
            
            
            if topNode.right:
                s.append(topNode.right)
                
            if topNode.left:
                s.append(topNode.left)
                
        return preorder
