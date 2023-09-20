class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        """
        Print the values of each Node in the Queue
        :return: None
        """
        temp = self.first

        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """
        Add a new Node at the end of the queue
        :param value: The value of the Node to be added
        :return: True when the Node is successfully added
        """
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return True

    def dequeue(self):
        """
        Remove the Node at the beginning of the queue
        :return: the removed Node
        """
        if self.length == 0:
            return None

        remove_node = self.first

        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = remove_node.next
            remove_node.next = None

        self.length -= 1
        return remove_node
