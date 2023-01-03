class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      if node.next == self.head:
        break 
      node = node.next


class Main:
  def run():
    Main.CreationDoublySLL()
    
  def CreationDoublySLL():
    doublyLinkedList = DoublyLinkedList()

    node1 = Node(1)
    node1.next = node1

    doublyLinkedList.head = node1
    doublyLinkedList.tail = node1

    print(f'Creation Doubly SLL => {[node.value for node in doublyLinkedList]}')

    
