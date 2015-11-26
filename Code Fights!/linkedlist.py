class Node:
  
  def __init__(self,data=None, next=None):
    self.data=data
    self.next=next
  
  def getData(self):
    return self.data
  
  def getNext(self):
    return self.next
  
  def setNext(self,newnext):
    self.next=newnext
  
class LinkedList:
  def __init__(self,head=None):
    self.head=LinkedList()
    self.head=head
    
  def insert(self, data):
    newnode=Node(data)
    self.head.setNext(newnode)
    self.head=newnode
  
l_list = LinkedList()
l_list.insert("David")
l_list.insert("Thomas")