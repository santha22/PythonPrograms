class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
            
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1
