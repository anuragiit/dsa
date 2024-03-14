class Node:
    def __init__(self,a):
        self.data=a
        self.next=None    

class Linkedlist:
    def __init__(self):
        self.head=None
    def len(self):
        count=0
        curr=self.head
        while curr:
            count+=1
            curr=curr.next
        return count
    
    def append_node(self,i):  # for adding at last
##        if self.head==None: 
##            self.head=Node(i)    Appending using one variable
##        else:    
##            curr=self.head
##            while curr.next:
##                curr=curr.next
##            curr.next=Node(i)
         current=head                       #Appending using two variables
         parent=head                  
         while current:
             parent=curr
             curr=curr.next
          parent.next=Node(i)
          
    def addNode(self,i,pos):
        if pos>self.len()+1:
            print("Wrong position given")
        elif pos==1:
            temp=Node(i)
            temp.next=self.head
            self.head=temp
    
        else:
            j=1
            curr=self.head
            while j<pos-1:
                curr=curr.next
                j+=1
            temp=Node(i)
            temp.next=curr.next
            curr.next=temp
            
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.data,'---------------->',end='')
            curr=curr.next
a=Linkedlist()
a.append_node(1)
a.append_node(3)
a.append_node(5)
a.append_node(7)
a.append_node(9)
a.append_node(11)
a.traverse()
b=a.len()
print('\n',b)
a.addNode(6,1)
a.addNode(13,5)
a.traverse()
print('\n',a.len())
