class Solution:
    def sumOfLeafNodes(self, root):
        #Your code here
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.data
            
        val = self.sumOfLeafNodes(root.left)
        val1 = self.sumOfLeafNodes(root.right)
        
        return val + val1
