class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Fila:
  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def push(self, elem):
    node = Node(elem)
    if self.last is None:
      self.last = node
    else:
      self.last.next = node
      self.last = node
    if self.first is None:
      self.first = node
    self.size = self.size +1

  def pop(self):
    if self.size > 0:
      elem = self.first.data
      self.first = self.first.next
      self.size = self.size -1
      return elem
    raise IndexError("Fila vazia")

  def rtn(self):
    if self.size > 0:
      elem = self.first.data
      return elem
    raise IndexError("Fila vazia")
  
  def __len__(self):
    return self.size

  def __repr__(self):
    if self.size > 0:
      r = ""
      ponteiro = self.first
      while(ponteiro):
        r = r + str(ponteiro.data) + " "
        ponteiro = ponteiro.next
      return r
    return "Fila vazia"  


  def __str__(self):
    return self.__repr__()    


