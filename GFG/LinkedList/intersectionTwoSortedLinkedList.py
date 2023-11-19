class Solution:
    def findIntersection(self,head1,head2):
        #return head
        ans = []
        temp = head1
        temp1 = head2
        flag = 0
        
        while temp is not None and temp1 is not None:
            if temp.data == temp1.data:
                flag = 1
                ans.append(temp.data)
                temp = temp.next
                temp1 = temp1.next
                
            else:
                if temp.data < temp1.data:
                    temp = temp.next 
                    
                else:
                    temp1 = temp1.next
                
        if flag == 0:
            return None
            
        head = None
        tail = None
        
        for it in ans:
            if head is None:
                head = Node(it)
                tail = head
                
            else:
                tail.next = Node(it)
                tail = tail.next
                
            
        return head
                
