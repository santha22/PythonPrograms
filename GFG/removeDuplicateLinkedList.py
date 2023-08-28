def removeDupliates(head):
    temp = head
    while temp.next:
        if(temp.data == temp.next.data):
            temp.next = temp.next.next
        else:
            temp = temp.next



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
        if(self.head is None):
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

    def printList(self):
        if(self.head is None):
            print(" ")
            return

        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next

        print("")

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().split()))
        for x in nodes:
            a.append(x)
        removeDupliates(a.head)
        a.printList()