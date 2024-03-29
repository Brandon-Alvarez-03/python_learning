"""
Basic Node example containing data and one link to another node.
The node's data will be specified when creating the node and immutable.
The link will be optional at initialization and can be updated.

Remember: At the end of a node path, th elink to the next node is null because there are no more nodes available. In Python, this means it will be set to None
"""

class Node():
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node

  def set_link_node(self, new_link_node):
    self.link_node = new_link_node

  def set_value(self, value):
    self.value = value

  ### Initiate 3 nodes for linking
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")
yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

