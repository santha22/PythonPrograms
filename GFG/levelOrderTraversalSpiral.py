from collections import deque

def findSpiral(root):
    if not root:
        return []

    even_stack = [root]
    odd_stack = []
    result = []

    while even_stack or odd_stack:
        while even_stack:
            node = even_stack.pop()
            result.append(node.data)

            if node.right:
                odd_stack.append(node.right)
            if node.left:
                odd_stack.append(node.left)

        while odd_stack:
            node = odd_stack.pop()
            result.append(node.data)

            if node.left:
                even_stack.append(node.left)
            if node.right:
                even_stack.append(node.right)
    return result


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
        result = findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()