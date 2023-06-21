from collections import deque
class Stack:
    def __init__(self):
        self.buffer = deque()

    def push(self,data):
        self.buffer.append(data)

    def pop(self):
        if len(self.buffer) == 0:
            print("empty stack")
            return
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    revstr = ""
    while stack.size()!=0:
        revstr+=stack.pop()

    return revstr

if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))
    print(reverse_string("I am the king"))



