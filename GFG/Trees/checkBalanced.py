class Solution:
    def dfsHeight(self, root):
        if root is None:
            return 0
            
        leftSub = self.dfsHeight(root.left)
        if leftSub == -1:
            return -1
            
        rightSub = self.dfsHeight(root.right)
        if rightSub == -1:
            return -1
            
        if abs(leftSub - rightSub) > 1:
            return -1
            
        return max(leftSub, rightSub) + 1
        
    
    def isBalanced(self,root):
    
        #add code here
        return self.dfsHeight(root) != -1

