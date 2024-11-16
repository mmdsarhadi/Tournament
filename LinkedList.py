class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.head.prev is None:
            self.head.prev = new_node
            new_node.next = self.head
            self.tail = new_node
            return
        self.tail.prev = new_node
        new_node.next = self.tail
        self.tail = new_node

    def delete(self):
        value = self.head.data
        self.head = self.head.prev
        return value
