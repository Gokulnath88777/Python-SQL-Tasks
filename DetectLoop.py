class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def traversal(self):
        temp=self
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    def checkLoop(self):
        slow=self
        fast=self
        count=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            count+=1
            if(slow==fast):
                print("count of the Loop",count)
                return 


# class LinkedList():
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         new_node=Node(data)
#         if(self.head is None):
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node
#     def display(self):
#         current=self.head
#         while current is not None:
#             print(current.data,end="->")
#             current=current.next
#         print(None)

# Manual Node creation
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head
head.checkLoop()



        