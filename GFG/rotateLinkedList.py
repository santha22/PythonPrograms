class Solution:
    def roate(self, head, k):
        temp = head
        temp1 = head

        i = 1
        while(temp and i < k):
            temp = temp.next
            i += 1

        if(temp is None or temp.next is None):
            return head

        head = temp.next
        temp.next = None
        temp = head

        while(temp.next):
            temp = temp.next

        temp.next = temp1

        return head


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

def printList(n):
    while(n):
        print(n.data, end=" ")
        n = n.next
    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        val = list(map(int, input().split()))
        ll = LinkedList()
        for i in val:
            ll.append(i)
        k = int(input())
        ob = Solution()
        printList(ob.roate(ll.head, k))
