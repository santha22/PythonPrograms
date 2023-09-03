class Solution:
    def sortedInsert(self, head, data):
        cur = head
        nxt = None
        prev = None

        dummy = Node(data)
        if(head.data > data):
            dummy.next = head
            while(cur.next != head):
                cur = cur.next
            cur.next = dummy
            return dummy

        while(cur.data < data):
            nxt = cur.next
            prev = cur
            cur = cur.next

        prev.next = dummy
        dummy.next = cur

        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def push(self, data):
        if(not self.head):
            nn = Node(data)
            self.head = nn
            self.last = nn
            nn.next = nn
            return
        nn = Node(data)
        nn.next = self.head
        self.last.next = nn
        self.last = nn

def printList(head):
    if(not head):
        return

    temp = head
    print(temp.data, end=" ")
    temp = temp.next
    while(temp != head):
        print(temp.data, end=" ")
        temp = temp.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        data = int(input())

        ll = LinkedList()
        for e in arr:
            ll.push(e)

        resHead = Solution().sortedInsert(ll.head, data)
        printList(resHead)