class Solution:
    def rearrange(self, head):
        # Code here
        temp = head
        ans = []

        while temp and temp.next:
            ans.append(temp.next.data)
            temp.next = temp.next.next
            if temp.next:
                temp = temp.next

        ll = LinkedList()
        for i in ans:
            ll.push(i)

        temp.next = ll.head

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
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ll = LinkedList()
        n = int(input())
        values = list(map(int, input().split()))
        for i in reversed(values):
            ll.push(i)

        Solution().rearrange(ll.head)
        ll.printList()
