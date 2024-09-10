class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def is_empty(self):
    return self.size == 0

  def append(self, value):
    new_Node = Node(value)
    if self.head is None:
      self.head = new_Node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_Node

  def add_first(self, value):
    new_Node = self.Node(value, self.head)
    self._head = new_Node

    if self.tail is None:
      self.tail = new_Node

    self.size += 1
  
  def remove_last(self):
    if self.is_empty():
      raise Empty('Book list is empty')
      answer = None
      if self._head._next is None:
        answer = self._head._element
        self._head = None
        self._tail = None
        self._size -= 1
        return answer

  def remove_first(self):
    if self.is_empty():
      raise Empty('Book list is empty')
    answer = self._head._element
    self._head = self._head._next
    self.size -= 1

    if self.is_empty():  # special case as the list is empty
      self.tail = None  # removed head had been the tail
    return answer

  def remove_by_value(self, value):