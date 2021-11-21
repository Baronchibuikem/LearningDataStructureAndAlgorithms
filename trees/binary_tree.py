"""
Question:
Implement a binary tree using Python, and show it's usuage with some example
"""

# Binary tree
class TreeNode:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    # convert the tuple arguments to a binary tree automatically
    def parse_tuple(self, data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = self.parse_tuple(data[0])
            node.right = self.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)

        return node

    # display the tree on the terminal
    def display_keys(self, node, space="\t", level=0):
        # if node is empty
        if node is None:
            print(space * level + "θ")
            return

        # if node is a leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return

        self.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        self.display_keys(node.left, space, level + 1)

    # traverse a tree inorder
    def traverse_in_order(self, node):
        if node is None:
            return []
        return (
            self.traverse_in_order(node.left)
            + [node.key]
            + self.traverse_in_order(node.right)
        )

    # traverse a tree pre-order
    def traverse_preoder(self, node):
        if node is None:
            return []
        return (
            [node.key]
            + self.traverse_preoder(node.left)
            + self.traverse_preoder(node.right)
        )

    # traverse a tree post-order
    def traverse_post_order(self, node):
        if node is None:
            return []

        return (
            self.traverse_post_order(node.left)
            + self.traverse_post_order(node.right)
            + [node.key]
        )

    # get the height of the tree
    def tree_height_or_max_depth(self, node: list) -> int:
        if node is None:
            return 0
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))

    # get the size of the tree
    def tree_size(self, node: list) -> int:
        if node is None:
            return 0
        return 1 + self.tree_size(node.left) + self.tree_size(node.right)

    def min_depth(self, node):
        if node is None:
            return 0
        return 1 + min(self.min_depth(node.left), self.min_depth(node.right))

    def remove_none(self, nums):
        return [x for x in nums if x is not None]

    def check_is_binary_search_tree(self, node):
        if node is None:
            return True, None, None

        is_bst_left, min_left, max_left = self.check_is_binary_search_tree(node.left)
        is_bst_right, min_right, max_right = self.check_is_binary_search_tree(
            node.right
        )

        min_key = min(self.remove_none([min_left, node.key, min_right]))
        max_key = min(self.remove_none([max_left, node.key, max_right]))

        is_bst_node = (
            is_bst_left
            and is_bst_right
            and (max_left is None or node.key > max_left)
            and (min_right is None or node.key < min_right)
        )

        return is_bst_node, min_key, max_key

    def insert(self, node, key, value=None):
        if node is None:
            node = TreeNode(key, value)

        elif key < node.key:
            node.left = self.insert(node.left, key, value)
            node.left.parent = node

        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            node.right.parent = node

        return node


# Create tree automatically
# first tuple is the left node
# single digit is the key or first root
# second tuple is the right node
tree_tuple = ((1, 3, 4), 2, ((None, 3, 4), 5, (6, 7, 8)))

# Create tree manually
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(8)


tree = root.parse_tuple(tree_tuple)

# A binary search tree is a binary tree that satisfies the following conditions
# 1 - The left subtree of any node only contains nodes with keys less than the node's key
# 2 - The right subtree of any node only contains nodes with keys greater than the node's key


# inserting a value to the tree
tree = TreeNode()
value = tree.insert(None, "micheal", "micheal")
tree.insert(value, "andy", "andy")
tree.insert(value, "kelechi", "kelechi")
tree.insert(value, "peace", "peace")
tree.insert(value, "ochez", "ochez")
tree.insert(value, "baron", "baron")
tree.insert(value, "favour", "favour")
tree.insert(value, "ochez", "ochez")

tree.display_keys(value)
