from _testcapi import INT_MIN


class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    MIN_LIMIT = -4294967296
    MAX_LIMIT = 4294967296

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

    def min_node(node:Node):
        if node is None:
            return node
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp


    def max_node(node:Node):
        if node is None:
            return None
        temp = node
        while temp.right is not None:
            temp = temp.right
        return temp

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

    def checkiflefttreeisBST(lefttree:Node, data):
        if lefttree is None or data >= lefttree.data:
            return True
        else:
            return False

    def checkifrihttreeisBST(righttree: Node, data):
        if righttree is None or data < righttree.data:
            return True
        else:
            return False

    def isBst_helper_Incorrect(treenode:Node):
        if treenode is None:
            return True

        left_tree = treenode.left
        right_tree = treenode.right
        if BST.checkiflefttreeisBST(left_tree, treenode.data) and BST.checkifrihttreeisBST(right_tree, treenode.data):
            BST.isBst_helper_Incorrect(left_tree)
            BST.isBst_helper_Incorrect(right_tree)
        else:
            return False
        return True

    def max_treenode(treenode:Node):
        if treenode is None:
            return None
        while treenode.right is not None:
            treenode = treenode.right

        return treenode.data

    def min_treenode(treenode:Node):
        if treenode is None:
            return None
        while treenode.left is not None:
            treenode = treenode.left

        return treenode.data

    def isBST_util_unefficient(nodetree:Node):
        if nodetree is None:
            return True

        left_node = nodetree.left
        right_node = nodetree.right

        if left_node is not None and not BST.max_treenode(left_node) <= nodetree.data:
            return False
        if right_node is not None and not BST.max_treenode(right_node) > nodetree.data:
            return True

        if BST.isBST_util_unefficient(left_node) and BST.isBST_util_unefficient(right_node):
            return True
        return  False

    def isBST_util_efficient(treenode:Node, min, max):
        if treenode is None:
            return True

        if treenode.data < max or treenode.data >= min:
            BST.isBST_util_efficient(treenode.left, min, treenode.data)
            BST.isBST_util_efficient(treenode.right, treenode.data, max)
            return True
        else:
            return False

    # Incorrect algo
    def isBst(self):
        return BST.isBST_util_efficient(self.root,BST.MIN_LIMIT, BST.MAX_LIMIT)

    def delete_util(node: Node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = BST.delete_util(node.left, key)
        elif key > node.data:
            node.right = BST.delete_util(node.right, key)
        else:
            if node.left and node.right is None:
                return None

            leftnode: Node = node.left
            rightnode: Node = node.right

            if rightnode is None:
                temp = Node(leftnode.data)
                node = temp
            elif leftnode is None:
                temp = Node(rightnode.data)
                node = temp
            else:
                temp_min_node:Node = BST.min_node(rightnode)
                node.data = temp_min_node.data
                node.right = BST.delete_util(rightnode, temp_min_node.data)

            return node





    def delete(self, key):
        return BST.delete_util(self.root, key)


#return BST.isBst_helper_Incorrect(self.root)






tree = BST()
tree.insert(14)
tree.insert(10)
tree.insert(16)
tree.insert(8)
tree.insert(20)
tree.insert(15)
tree.insert(18)
tree.insert(19)

print(tree.delete(16))
tree.depth_order_traversal()