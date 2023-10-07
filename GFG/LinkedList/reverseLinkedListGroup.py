class Solution:
    def reverse(self, head, k):
        prev = None
        cur = head
        nxt = None
        count = 0

        while (cur is not None) and (count < k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1

        if cur is not None:
            head.next = self.reverse(cur, k)

        return prev


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end= " ")
            temp = temp.next
        print()

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
            
        k = int(input())
        new_head = LinkedList()
        ob = Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
