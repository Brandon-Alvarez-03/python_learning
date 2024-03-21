# Define your Node class below:
# Each linked list is a sequential chain of nodes.
## This means the first step is building out a node class
### A node contains two elements:
###   - data
###   - a link to the next node
class Node():
  # initialize both value and next_node pointer for node instance (defaults next node as Null or None)
  def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node

  # returns the value of this node
  def get_value(self):
    return self.value

  # returns the "address" of the next_node in the linked list, whcih this node is pointing to
  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)
    