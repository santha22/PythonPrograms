class Solution:
    def check(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 == root2
            
        return (root1.data == root2.data) and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)
        
    
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here 
        if root is None:
            return True 
            
        if root.left is None or root.right is None:
            return root.left == root.right 
            
        return self.check(root.left, root.right)
