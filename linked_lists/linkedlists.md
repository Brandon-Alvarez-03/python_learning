# Linked Lists and Doubly Linked Lists

This unit covers:

- Create and use Node classes in Python
- Create and use LinkedList class in Python using prior Node classes
- Use common LinkedList algorithms
- Create and use DoublyLinkedList classes in Python with an implementation of edited versions of Node class

Lastly, will develop a portfolio project ot reinforce concepts

## Nodes

### What is a node?

Nodes are the fundamental building blocks of data structures
They form the basis for:

- linked lists
- stacks
- queues
- trees

Individual nodes contain data and links to other nodes.
Each data structure adds additional constraints or behavior to these features. to create the desired structure.

eg.

```python
node_a = {"Data": 5, "Link": node_b}
```

### Node implementations

Nodes can contain a variety of data types

- int
- float
- dec
- arr
- null

and so on.

The link or links within the node are sometimes referred to as pointers because they "point" to other nodes.

Typically, data structures are implement nodes with one or more links.
If the links are `null` or `None`, it denotes that you have reached the end of the particular node or link path you were previously following.

Scenarios:

- node points to another node which has null link indicating end of list ro path
- a node can point to several nodes which either conntinue linking forward or end with null
- a node can point to another node (which points backward to the intital node)

### Node linking

Often, due to the data structure, nodes may only be linked to a single other node.
This makes considering how you modify or remove nodes from a data structure very important.

If you inadvertently remove the single link to a node, that node's data and any linked nodes could be "lost" to your application.

When this happens to a node, is is called an 'orphaned' node.
