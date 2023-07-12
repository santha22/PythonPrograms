class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def dfs(lower, upper, node):
            if not node:
                return True
            elif node.data <= lower or node.data >= upper:
                return False
            else:
                return dfs(lower, node.data, node.left) and dfs(node.data, upper, node.right)
        return dfs(float('-inf'), float('inf'), root)
