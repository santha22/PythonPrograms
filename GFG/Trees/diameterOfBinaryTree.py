class Solution:
    def f(self, root, dm):
        if root is None:
            return 0
            
        left = self.f(root.left, dm)
        right = self.f(root.right, dm)
        dm[0] = max(dm[0], left + right)
        
        return max(left, right) + 1
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        dm = [0]
        self.f(root, dm)
        return dm[0] + 1
