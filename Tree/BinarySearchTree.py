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

    def min(self):
        current:Node = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left

        return current.data

    def max(self):
        current:Node = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right

        return current.data

    def hight_of_tree(root:Node):
        if root is None:
            return -1

        left_tree = BST.hight_of_tree(root.left)+1
        right_tree = BST.hight_of_tree(root.right) +1

        return BST.maxValue(left_tree, right_tree)

    def maxValue(leftnodedata, rightnodedata):
        if leftnodedata >= rightnodedata:
            return leftnodedata
        else: return rightnodedata

    def tree_Heigh(self):
        if self.root is None:
            return 0
        return BST.hight_of_tree(self.root)


tree = BST()
tree.insert(4)
tree.insert(5)
tree.insert(1)
tree.insert(2)
print(tree.tree_Heigh())
