class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def display(self,node):
        current=head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print(None)
    def removeDuplicate(self,node):
        current=head
        while current and current.next:
            if(current.data==current.next.data):
                current.next=current.next.next
            current=current.next

head=Node(10)
head.next=Node(10)
head.next.next=Node(20)
head.next.next.next=Node(20)
head.next.next.next=Node(30)
obj=LinkedList()
obj.removeDuplicate(head)
obj.display(head)

