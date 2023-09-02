class Solution:
    def palindrome(self, head):
        stack = []
        start = 1
        end = 0
        temp = head
        while(temp):
            end += 1
            stack.append(temp.data)
            temp = temp.next

        while(start < end):
            if(stack.pop() == head.data):
                start += 1
                end -= 1
                head = head.next
            else:
                return False
            
        return True

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

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ll = LinkedList()
        for i in arr:
            ll.append(i)
        if(Solution().palindrome(ll.head)):
            print(1)
        else:
            print(0)
