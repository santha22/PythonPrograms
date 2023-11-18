class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        
        
        temp = head
        temp1 = head.next
        
        while temp1 is not None:
            dummy = temp.next
            temp.next = temp.prev
            temp.prev = dummy
            
            temp = temp.prev
            temp1 = temp1.next
            
        dummy = temp.next
        temp.next = temp.prev
        temp.prev = dummy 
        
        return temp
