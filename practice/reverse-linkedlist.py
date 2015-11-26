class Node: 
  def __init__(self, data=None, next=None): 
    self.dat = data
    self.cdr = next    
  def __str__(self): 
    return str(self.dat)
  
  #def reverse(self):
    
  def add(self, data):
    nextnode=Node()
    nextnode.dat=data
    self.cdr = nextnode
  
nodo = Node()
nodo.add(4)
print nodo.cdr

