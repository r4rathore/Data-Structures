class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data= None):
        self.root = None

    def insert_helper(node:Node, data):
        if node is None:
            return Node(data)

        if data <= node.data:
            node.left = BST.insert_helper(node.left, data)
        else:
            node.right = BST.insert_helper(node.right, data)

        return  node

    def insert(self, data):
        self.root = BST.insert_helper(self.root, data)

tree = BST()
tree.insert(4)
tree.insert(5)
tree.insert(1)
tree.insert(2)

