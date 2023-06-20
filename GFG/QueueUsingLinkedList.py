class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = self.rear = None
        self.length = 0

    def push(self,item):
        newNode = Node(item)
        if self.length == 0:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        temp = self.front
        self.front = temp.next
        self.length -= 1

        if self.length == 0:
            self.rear = None
        temp.next = None
        return temp.data


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i <len(q1)):
            if(q1[i] == 1):
                s.push(q1[i+1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(),end=" ")
                i = i+1
            elif(s.isEmpty()):
                print(-1)
        print()