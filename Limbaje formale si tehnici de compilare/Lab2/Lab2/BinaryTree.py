class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if self.value is None:
            self.value = value
            return
        if self.value == value:
            return
        if value < self.value:
            if self.left is not None:
                self.left.add_node(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right is not None:
                self.right.add_node(value)
            else:
                self.right = BinarySearchTree(value)

    def search(self, value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        if value < self.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return False
        if value > self.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return False

    def inorder_traversal(self, stored_values: list):
        if self.left is not None:
            self.left.inorder_traversal(stored_values)
        if self.value is not None:
            stored_values.append(self.value)
        if self.right is not None:
            self.right.inorder_traversal(stored_values)
        return stored_values









































































