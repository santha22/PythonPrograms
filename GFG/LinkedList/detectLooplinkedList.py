class Solution:
    def detectLoop(self, head):
        if (head == None):
            return False

        elif head.next == None:
            return False

        else:
            slow = head
            fast = head.next
            while (slow and fast and fast.next):
                if (slow == fast):
                    return True
                else:
                    slow = slow.next
                    fast = fast.next.next
            return False


# Node Class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def loopHere(self, pos):
        if pos == 0:
            return
        walk = self.head
        for i in range(1, pos):
            walk = walk.next
        self.tail.next = walk

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next




if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        ll = LinkedList()
        for i in input().split():
            ll.insert(int(i))

        ll.loopHere(int(input()))
        print(Solution().detectLoop(ll.head))
