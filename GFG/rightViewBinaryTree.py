class Solution:
    def rightView(self, root):
        if not root:
            return []

        q = deque([(0, root)])
        ans = []

        while q:
            level, node = q.popleft()

            if len(ans) == level:
                ans.append(node.val)
            else:
                ans[level] = node.val

            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        return ans

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightView(self, root):
        if not root:
            return []

        q = deque([(0, root)])
        ans = []

        while q:
            level, node = q.popleft()

            if len(ans) == level:
                ans.append(node.val)
            else:
                ans[level] = node.val

            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        return ans

# Test the code
# Assuming you have constructed your binary tree, e.g., root = TreeNode(1)
# and connected the nodes as per your requirement.

# Initialize the solution object
sol = Solution()

# Get the right view of the binary tree
result = sol.rightView(root)

# Print the result
print(result)

