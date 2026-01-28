class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node
    def insertAtBegining(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def afterNode(self,prev_node,data):
        new_node=Node(data)
        current=self.head
        while current!=None and current.data!=prev_node:
            current=current.next
        if not current:
            print("Previous node Not found")
        else:
            new_node.next=current.next
            current.next=new_node
    def delNode(self,data):
        if not self.head:
            print("List is Emplty")
            return
        else:
            current=self.head
            if self.head.data==data:
                self.head=self.head.next
            else:
                while current.next!=None and current.next.data!=data:
                    current=current.next
                if current.next==None:
                    print("There is no such a element")
                else :
                    current.next=current.next.next
            
        
    def display(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next
    
obj=LinkedList()
obj.append(10)
obj.append(20)
obj.insertAtBegining(0)
obj.afterNode(20,10000)
obj.delNode(0)
obj.display()


        