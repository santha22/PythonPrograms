class Solution:
    def inOrder(self, root):
        # code here
        s = []
        node = root
        inorder = []
        
        while True:
            if node:
                s.append(node)
                node = node.left
                
            else:
                if len(s) == 0:
                    break
                
                node = s.pop()
                inorder.append(node.data)
                node  = node.right
                
        return inorder
