class Solution:
    def pairWiseSwap(self, head):
        # code here
        dummy = Node(0)
        dummy.next = head
        point = dummy

        while point.next and point.next.next:
            # save ptrs
            swap1 = point.next
            swap2 = point.next.next

            # reverse this pair
            swap1.next = swap2.next
            swap2.next = swap1

            # Update ptrs
            point.next = swap2
            point = swap1

        return dummy.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isnert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head

        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=" ")
        n = n.next

    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        li = LinkedList()
        for i in arr:
            li.isnert(i)

        dict1 = {}
        temp = li.head
        while temp:
            dict1[temp] = temp.data
            temp = temp.next

        failure = LinkedList()
        failure.isnert(-1)

        head = Solution().pairWiseSwap(li.head)

        temp = head
        f = 0
        while temp:
            if dict1[temp] != temp.data:
                f = 1;
            temp = temp.next

        if f:
            printList(failure)

        else:
            printList(head)