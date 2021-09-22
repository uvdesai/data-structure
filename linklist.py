class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linklist:
    def __init__(self):
        self.head=None
    
    def print(self):
        if self.head is None:
            print("the link list is empty")
            return
        new=self.head
        total=" "
        while new:
            total+=str(new.data)+'-->'
            new=new.next
        print(total)
    def insert_at_began(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def remove_by_index(self,index):
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                 itr.next=itr.next.next
            itr=itr.next
            count+=1
    def remove_by_value(self,data):
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
            itr=itr.next



        
        


if __name__ == '__main__':
    ll=Linklist()
    ll.insert_at_began(5)
    ll.insert_at_began(67)
    ll.insert_at_end(45)
    ll.remove_by_value(67)
  #  ll.remove_by_index(1)
    ll.print()



