class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, key):
        # code here
        if root is None:
            return Node(key)
        
        
        if key == root.data:
            return root

        # Recur down the tree.
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return root
            
