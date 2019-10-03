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

    def preorder_traversal_helper(treenode:Node):
        if treenode is None:
            return None
        print(treenode.data)
        BST.preorder_traversal_helper(treenode.left)
        BST.preorder_traversal_helper(treenode.right)

    def traverse_preorder(self):
        return BST.preorder_traversal_helper(self.root)

    def inorder_traversal_helper(treenode:Node):
        if treenode is None:
            return
        BST.inorder_traversal_helper(treenode.left)
        print(treenode.data)
        BST.inorder_traversal_helper(treenode.right)


    def traverse_inorder(self):
        return  BST.inorder_traversal_helper(self.root)

    def preorder_traversal_helper(treenode:Node):
        if treenode is None:
            return
        BST.inorder_traversal_helper(treenode.left)
        BST.inorder_traversal_helper(treenode.right)
        print(treenode.data)

    def traverse_preorder(self):
        return  BST.preorder_traversal_helper(self.root)

    def deptorder_helper(node_queue:list):
        if (node_queue is None) or (len(node_queue) <= 0):
            return
        else:
            new_queue = []
            for node in node_queue:
                print(node.data)
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)

            return BST.deptorder_helper(new_queue)


    def depth_order_traversal(self):
        node_queue: list = [self.root]
        return BST.deptorder_helper(node_queue)








tree = BST()
tree.insert(14)
tree.insert(10)
tree.insert(16)
tree.insert(8)
tree.insert(9)
tree.insert(15)
tree.insert(18)

tree.depth_order_traversal()
