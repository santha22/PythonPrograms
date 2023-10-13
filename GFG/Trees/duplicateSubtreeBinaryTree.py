class Solution:
    def solve(self, node, hmap):
        sb = []
        
        # return n if there is no left node or right node
        if not node:
            return "n"
            
        if not node.left and not node.right:
            return str(node.data)
            
        sb.append(self.solve(node.left, hmap))
        sb.append(self.solve(node.right, hmap))
        sb.append(str(node.data))
        
        key = "".join(sb)
        
        hmap[key] = hmap.get(key, 0) + 1
        
        return key
        
    
    def dupSub(self, root):
        # code here 
        hmap = {}
        
        self.solve(root.left, hmap)
        self.solve(root.right, hmap)
        
        for key, value  in hmap.items():
            if value > 1:
                return 1
                
        return 0
