# Implementation of staks usin Double Link List

class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkList:
    def __init__(self):
        self.head = Node()

    def push(self, value):
        new_Node = Node(value)
        current_Head = self.head

        if current_Head.data is None:
            self.head = new_Node
            return self.head

        new_Node.next = current_Head
        current_Head.prev = new_Node
        self.head = new_Node
        return self.head

    def pop(self):
        current_head = self.head
        result = None

        if current_head is None:
            return ('stack is empty')

        if (current_head.next is None) & (current_head.prev is None):
            result = current_head.data
            current_head = None
            return result

        result = current_head.data
        current_head = current_head.next
        self.head = current_head
        return result


dll = DoubleLinkList()
dll.push(1)
dll.push(3)
dll.push(4)
dll.push(2)

print(dll.pop())
print(dll.pop())
print(dll.pop())
print(dll.pop())
print(dll.pop())