#understanding linked list in python
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
    
    def insert_list(self,list_data):
        for data in list_data:
            self.head = Node(data,self.head)
    
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        
        return count

    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
        
        count =0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    
    def insert_at(self,index,data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
            
        if index ==0:
            self.insert_at_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1



    def prints(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
    
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        count =0
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
            itr = itr.next
            count +=1

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        count =0
        while itr:
            if itr.data == data:
                itr.data = itr.next.data
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list(['mango','orange','apple','pappaya'])
    ll.insert_after_value('apple','jackfruit')
    ll.prints()
    ll.remove_by_value('jackfruit')
    ll.prints()