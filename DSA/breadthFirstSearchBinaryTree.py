import collections


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

def makeList(root):
    if root is None:
        return
    else:
        d[root.data] = []
        makeList(root.left)
        if root.left:
            d[root.data].append(root.left.data)
        if root.right:
            d[root.data].append(root.right.data)
        makeList(root.right)

    return d

def bfs(al):
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    print(visited)


"""def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root"""

if __name__ == '__main__':
    #letters = ['g', 'c', 'b', 'a', 'e', 'd', 'f', 'i', 'h', 'j', 'k']
    root = BinarySearchTreeNode('g')
    root.add_child('c')
    root.add_child('b')
    root.add_child('a')
    root.add_child('e')
    root.add_child('d')
    root.add_child('f')
    root.add_child('i')
    root.add_child('h')
    root.add_child('j')
    root.add_child('k')

    d = {}
    aList = makeList(root)

    """for ele in aList:
        print(f'{ele}:{d[ele]}')
"""
    bfs(aList)






