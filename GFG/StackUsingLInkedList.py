class MyStack:

    def __init__(self):
        self.top = None

    # Function to push an integer into the stack.


    def push(self, data):
        # Add code here
        newNode = StackNode(data)
        if self.top == None:
            self.top = newNode
        else:
            currentTop = self.top
            self.top = newNode
            self.top.next = currentTop

        # Function to remove an item from top of the stack.


    def pop(self):
        # Add code here
        if self.top == None:
            return -1
        if self.top.next == None:
            result1 = self.top.data
            self.top = None
            return result1
        else:
            currentSecond = self.top.next
            result = self.top.data
            del self.top
            self.top = currentSecond
            return result


class StackNode:
    def __init__(self, data):   # 5   1 2 1 3 2 1 4 2    output 3 4
        self.data =  data
        self.next = None

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
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