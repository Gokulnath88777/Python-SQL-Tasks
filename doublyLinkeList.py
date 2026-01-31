class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
           current=self.head
           while current.next is not None:
               current=current.next
           current.next=new_node
           new_node.prev=current
    def insertAtBegining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def delNode(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                if current.prev is None:
                    self.head=current.next
                    if current.next is not None:
                        current.next.prev=None
                elif current.next is None:
                    current.prev.next=None
                else:
                    
                    current.next.prev=current.prev
                    current.prev.next=current.next
                return
            current=current.next
    def insert_after(self,target,data):
        current=self.head
        new_node=Node(data)
        while current is not None:
            if(current.data==target):
                new_node.next=current.next
                new_node.prev=current
                if current.next:
                    current.next.prev=new_node
                current.next=new_node
                return
            current=current.next
        print("Target not fount")
    def printForward(self):
        current=self.head
        while current is not None:
            print(current.data,end="<->")
            current=current.next
        print(None)
    def printBackward(self):
        current=self.head
        while current.next is not None:
            current=current.next
        while current is not None:
            print(current.data,end="<->")
            current=current.prev
        print(None)
        
obj=LinkedList()
obj.append(20)
obj.append(30)
obj.insertAtBegining(0)
obj.insert_after(30,100)
obj.printForward()
print()
obj.printBackward()

            
            



                    
                

