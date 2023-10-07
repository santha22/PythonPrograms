

def getNthFromLast(head,n):
    #code here
    count = 0
    temp = head
    temp1 = head
    while temp:
        count += 1
        temp = temp.next

    if n > count:
        return -1
    count = count - n
    for i in range(count):
        temp1 = temp1.next
    return temp1.data




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        nth_node = int(input())              #map(int, input().strip().split())
        a = LinkedList()
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        print(getNthFromLast(a.head,nth_node))
