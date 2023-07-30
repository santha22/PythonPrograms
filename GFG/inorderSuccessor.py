class Solution:
    def inorderSuccessor(self, root, x):
        successor = Node(-1)
        while(root is not None):
            if(x.data >= root.data):
                root = root.right
            else:
                successor = root
                root = root.left
        return successor



from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def buildTree(s):

    if(len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size + 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size -1

        currVal = ip[i]

        if(currVal != "N"):
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size = size + 1
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        if(currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i+1
    return root

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        root = buildTree(s)
        k = int(input())
        ptr = Solution().inorderSuccessor(root, Node(k))
        if ptr is None:
            print(-1)
        else:
            print(ptr.data)