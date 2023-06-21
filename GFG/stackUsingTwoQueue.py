# Function to push an element into stack using two queues.
def push(x):
    # global declaration
    global queue_1
    global queue_2
    queue_1.append(x)

    # code here


# Function to pop an element from stack using two queues.
def pop():
    # global declaration
    global queue_1
    global queue_2

    ans = -1

    while len(queue_1) > 1:
        queue_2.append(queue_1.pop(0))
    if len(queue_1) == 1:
        ans = queue_1.pop(0)

    while len(queue_2) > 0:
        queue_1.append(queue_2.pop(0))

    return ans

    # code he

q