class Solution:
    def segregate(self, head):
        h = LinkedList()
        l = []
        temp = head
        while temp:
            l.append(temp.data)
            temp = temp.next
        l.sort()

        for i in l:
            h.append(i)
        return h.head

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
        self.tail.next = new_node
        self.tail = new_node

def printList(head):
    if head is None:
        print(" ")
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print()

if __name__ == "__main__":
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().split()))
        for x in nodes:
            a.append(x)
        printList(Solution().segregate(a.head))