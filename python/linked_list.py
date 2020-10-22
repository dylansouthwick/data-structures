class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self,data):
    self.head = Node(data)

  def add(self, data):
    current = self.head
    while current.next is not None:
      current = current.next
    current.next = Node(data)

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pass

  def get(self, element_to_get):
    # 1 2 3 4
    # target : 5

    current = self.head
    while current is not None and current.data != element_to_get:
      # current = Node(4)
      current = current.next # current = None
    
    return current if current else False

  def __str__(self):
    answer = []
    current = self.head
    while current is not None:
      answer.append(current.data)
      current = current.next
    return str(answer)

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self,data,next = None):
    self.data = data
    self.next = next


ll = LinkList(0)
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
print(ll)
print('getting 2:',ll.get(2).data)
print('getting 5: ',ll.get(5))