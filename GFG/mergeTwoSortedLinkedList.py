def sortedList(head1, head2):
    dummy = Node(0)
    temp = dummy

    while(head1 and head2):
        if(head1.data < head2.data):
            temp.next = head1
            head1 = head1.next

        else:
            temp.next = head2
            head2 = head2.next

        temp = temp.next

    if(head1):
        temp.next = head1
    if(head2):
        temp.next = head2

    return dummy.next





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        newNode = Node(val)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode

        self.tail.next = newNode
        self.tail = newNode

def printL(n):
    while(n):
        print(n.data, end=" ")
        n = n.next


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().split()))
        valN = list(map(int, input().split()))
        ll1 = LinkedList()
        for i in valN:
            ll1.append(i)

        ll2 = LinkedList()
        valM = list(map(int, input().split()))
        for i in valM:
            ll2.append(i)

        head = sortedList(ll1.head, ll2.head)


        printL(head)