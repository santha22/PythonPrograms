class Solution:
    def addTwoLists(self, first, second):
        stack1 = []
        stack2 = []

        while first:
            stack1.append(first.data)
            first = first.next

        while second:
            stack2.append(second.data)
            second = second.next

        carry = 0
        result = None

        while stack1 or stack2 or carry:
            sum_val = carry
            if stack1:
                sum_val += stack1.pop()
            if stack2:
                sum_val += stack2.pop()

            carry = sum_val // 10
            new_node = Node(sum_val % 10)
            new_node.next = result
            result = new_node

        return result

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):

        if(self.head is None):
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while(n):
        print(n.data, end=" ")
        n = n.next
    print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nV = list(map(int, input().split()))
        ll1 = LinkedList()
        for i in nV:
            ll1.append(i)

        m = int(input())
        mV = list(map(int, input().split()))
        ll2 = LinkedList()
        for i in mV:
            ll2.append(i)

        res = Solution().addTwoLists(ll1.head, ll2.head)
        printList(res)

