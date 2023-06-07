class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head,None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None,itr)


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def insert_at(self,index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalied index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1




    def print_forward(self):
        if self.head is None:
            print("doubly linked list is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

    def print_backward(self):
        if self.head is None:
            print("doubly linked list is empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.prev
        print("Link list in reverse: ", listr)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    li = DoublyLinkedList()
    li.insert_values(["banana", "mango", "grapes", "orange"])
    li.print_forward()
    li.print_backward()
    li.insert_at_end("figs")
    li.print_forward()
    li.insert_at(0, "jackfruit")
    li.print_forward()
    """li.insert_at(6,"dates")
    li.print_forward()"""
    li.insert_at(2,"kiwi")
    li.print_forward()