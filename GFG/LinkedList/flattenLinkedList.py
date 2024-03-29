def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp

    while(a is not None and b is not None):
        if(a.data < b.data):
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom

    if(a is not None):
        temp.bottom = a
    else:
        temp.bottom = b

    return res.bottom
def flatten(root):
    if(root is None or root.next is None):
        return root

    root.next = flatten(root.next)

    root = mergeTwoLists(root, root.next)

    return root

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def printList(node):
    while(node is not None):
        print(node.data, end=" ")
        node = node.bottom
    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        head = None
        N = int(input())
        arr = []
        arr = [int(x) for x in input().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if(flag == 1):
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1
            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if(flag1 == 1):
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)
