def findCommon(self, root1, root2):
    # code here
    hmap = {}
    ls = []
    self.inorder(root1, hmap, ls, False)
    self.inorder(root2, hmap, ls, True)
    return ls
        
def inorder(self, root, hmap, ls, flag):
    if root is None:
        return 
    
    self.inorder(root.left, hmap, ls, flag)
    if not flag:
        hmap[root.data] = hmap.get(root.data, 0) + 1
        
    if flag and root.data in hmap:
        ls.append(root.data)
        
    self.inorder(root.right, hmap, ls, flag)
    
