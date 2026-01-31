class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:   
    def display(self):
        current=self
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print(None)
    def merge(self,list1,list2):
        dummy=Node(0)
        tail=dummy
        while list1 and list2:
            if list1.data<list2.data:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        current=head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print(None)                
                
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)


front=Node(100)
front.next=Node(200)
front.next.next=Node(500)
front.next.next.next=Node(600)

merge_head=LinkedList()
merge_head.merge(head,front)
