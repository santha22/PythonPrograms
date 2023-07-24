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
