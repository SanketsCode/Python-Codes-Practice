class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert_at_begining(self,data):
        if self.head == None:
            node = Node(data, None,self.head)
            self.head = node
        else:
            node = Node(data, None,self.head)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,itr,None)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        
        return count

    def prints(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next
        
        print(llstr)


        
    

        # count = self.get_length() -1
        # i=0
        # while itr:
        #     if i == count:
        #         print(itr.data)
        #     itr = itr.next
        #     i+=1
        # llstr = ''
        # itr = self.prev
        # while itr:
        #     print(itr.data)
        #     itr = itr.prev

            






if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(45)
    ll.insert_at_begining(5)
    ll.insert_at_begining(15)
    ll.insert_at_end(3)
    ll.prints()
    