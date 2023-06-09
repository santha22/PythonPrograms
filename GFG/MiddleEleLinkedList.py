


class Solution:
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        itr = head
        length = 0
        while itr is not None:
            length += 1
            itr = itr.next
        mid = length // 2
        temp = head
        for i in range(mid+1):
            if mid == i:
                return temp.data
            temp = temp.next






class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail =None

    def insert(self,data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


"""ll = Linked_List()
ll.insert(2)
ll.insert(4)
ll.insert(6)
ll.insert(7)
ll.insert(5)
ll.insert(1)
ob = Solution()
print(ob.findMid(ll.head))"""

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution
        print(ob.findMid(list1.head))


