class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse(self):
    prev = None
    current = self.head
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def insertion_sort(self):
    sorted_list = LinkedList()
    current = self.head
    while current:
      next = current.next
      sorted_list.sorted_insert(current.data)
      current = next
    self.head = sorted_list.head

  def sorted_insert(self, data):
    new_node = Node(data)
    if self.head is None or self.head.data >= data:
      new_node.next = self.head
      self.head = new_node
    else:
      current = self.head
      while current.next and current.next.data < data:
        current = current.next
      new_node.next = current.next
      current.next = new_node

  @staticmethod
  def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 and list2:
      if list1.data < list2.data:
        tail.next, list1 = list1, list1.next
      else:
        tail.next, list2 = list2, list2.next
      tail = tail.next
    tail.next = list1 or list2
    return dummy.next
