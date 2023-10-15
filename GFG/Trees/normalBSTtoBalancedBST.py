class Solution:
    def inorder(self, root, ls):
        if root is None:
            return
        
        self.inorder(root.left, ls)
        ls.append(root)
        self.inorder(root.right, ls)
        
    def bbst(self, ls, l, r):
        if l > r:
            return None
            
        mid = (l + r) // 2
        root = ls[mid]
        root.left = self.bbst(ls, l, mid-1)
        root.right = self.bbst(ls, mid+1, r)
        
        return root
    
    
    def buildBalancedTree(self,root):
        #code here
        ls = []
        self.inorder(root, ls)
        return self.bbst(ls, 0, len(ls)-1)
       
