class Linked:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
            return
        currenttop = self.top
        self.top = node
        self.top.next = currenttop

    def pop(self):
        if self.top == None:
            return
        if self.top.next == None:
            self.top = None
            return
        currentSecond = self.top.next
        del self.top
        self.top = currentSecond

    def peek(self):
        return self.top.data

    def printStack(self):
        print("\n")
        node = self.top
        while node != None:
            print(node.data)
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


ll = Linked()
ll.push(11)
ll.push(55)
ll.push(34)
ll.push(666)
ll.push(777)
ll.printStack()

ll.pop()
ll.printStack()
