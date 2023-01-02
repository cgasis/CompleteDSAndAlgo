class Node:

  def __init__(self, value=None):
    self.value = value
    self.next = None


class SinglyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  def insert(self, value, location):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      if location == 0:  #first node
        newNode.next = self.head
        self.head = newNode
      elif location == -1:  #last node
        newNode.next = None
        self.tail.next = newNode
        self.tail = newNode
      else:  #middle
        tempNode = self.head
        index = 0
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        nextNode = tempNode.next
        tempNode.next = newNode
        newNode.next = nextNode
        if tempNode == self.tail:
          self.tail = newNode

  def traverse(self):
    if self.head is None:
      print('The Singly Linked List is Null')
    else:
      print('Traverse SSL')
      node = self.head
      while node is not None:
        print(node.value)
        node = node.next

  def search(self, value):
    if self.head is None:
      print('The Singly Linked List is Null')
    else:
      searchNode = Node(value)
      node = self.head
      while node is not None:
        # print(node.value)
        if node.value == searchNode.value:
          return searchNode.value
        node = node.next
      print(f'The node {searchNode.value} has not found in SLL')
  
  def remove(self, location):
    if self.head is None:
      print('The Singly Linked List is Null')
    else:
      if location == 0:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
      elif location == -1:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          node = self.head
          while node is not None:
            if node.next == self.tail:
              break;
            node = node.next
          node.next = None
          self.tail = node
      else:
        tempNode = self.head
        index = 0
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        nextNode = tempNode.next
        tempNode.next = nextNode.next

  def removeAll(self):
    if self.head is None:
      print('The Singly Linked List is Null')
    else:
      self.head = None
      self.tail = None
        
class Main:

  def run():
    Main.creationSLL()
    Main.InsertionSLL()
    Main.TraverseSLL()
    Main.SearchSLL()
    Main.RemoveSLL()
    Main.RemoveAllSLL()

  def creationSLL():
    # Creation SLL
    # 1 create head and tail and reference to null
    # 2 create a blank node and assign value to it and     reference to null
    # 3 link head and tail to this node

    singlyLinkedList = SinglyLinkedList()
    node1 = Node(1)
    node2 = Node(2)

    singlyLinkedList.head = node1
    singlyLinkedList.head.next = node2
    singlyLinkedList.tail = node2

    print(f'Creation SLL => {[node.value for node in singlyLinkedList]}')

  def InsertionSLL():
    #Insertion SLL Algorithm
    singlyLinkedList = SinglyLinkedList()
    singlyLinkedList.insert(1, 1)
    singlyLinkedList.insert(2, 1)
    singlyLinkedList.insert(3, 2)
    singlyLinkedList.insert(4, 3)
    # singlyLinkedList.insertSLL(5,-1)
    print(f'Insertion SLL => {[node.value for node in singlyLinkedList]}')

  def TraverseSLL():
   singlyLinkedList = SinglyLinkedList()

   singlyLinkedList.insert(1, 1)
   singlyLinkedList.insert(2, 1)
   singlyLinkedList.insert(3, 2)

   singlyLinkedList.traverse()

  def SearchSLL():
   singlyLinkedList = SinglyLinkedList()

   singlyLinkedList.insert(1, 1)
   singlyLinkedList.insert(2, 1)
   singlyLinkedList.insert(3, 2)

   print(f'Search SSL')
   print(singlyLinkedList.search(4))

  def RemoveSLL():
   singlyLinkedList = SinglyLinkedList()

   singlyLinkedList.insert(1, 1)
   singlyLinkedList.insert(2, 1)
   singlyLinkedList.insert(3, 2)

   print(f'Remove SLL => {[node.value for node in singlyLinkedList]}')
   singlyLinkedList.remove(1)
   print(f'Remove SLL => {[node.value for node in singlyLinkedList]}')

  def RemoveAllSLL():
   singlyLinkedList = SinglyLinkedList()

   singlyLinkedList.insert(1, 1)
   singlyLinkedList.insert(2, 1)
   singlyLinkedList.insert(3, 2)

   print(f'Remove All SLL => {[node.value for node in singlyLinkedList]}')
   singlyLinkedList.removeAll()
   print(f'Remove All SLL => {[node.value for node in singlyLinkedList]}')
