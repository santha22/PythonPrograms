def Push(x,stack1,stack2):
    while(stack1):
        stack2.append(stack1.pop())

    stack1.append(x)
    while(stack2):
        stack1.append(stack2.pop())

def Pop(stack1,stack2):
    if len(stack1)==0:
        return -1

    return stack1.pop()

if __name__ == "__main__":
    t = int(input())
    for cases in range(t):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))
        i = 0
        stack1 = []
        stack2 = []
        while i<len(qtyp_qry):
            if qtyp_qry[i] == 1:
                Push(qtyp_qry[i+1], stack1,stack2)
                i+=2
            else:
                print(Pop(stack1,stack2), end=' ')
                i+=1
        print()