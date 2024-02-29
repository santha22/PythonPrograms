class Solution:
    def f(self, root, maxi):
        if root is None:
            return 0
            
        left = max(0, self.f(root.left, maxi))
        right = max(0, self.f(root.right, maxi))
        
        maxi[0] = max(maxi[0], left + right + root.data)
        
        return max(left, right) + root.data
    
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        maxi = [float("-inf")]
        self.f(root, maxi)
        return maxi[0]
