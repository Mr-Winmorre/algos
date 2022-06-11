class BstAlgo:
    def __init__(self, data):
        self.left_node = None
        self.right_node = None
        self.data = data

    def insert(self, val):
        if not self.data:
            self.data = val
            return

        if self.data == val:
            return

        if val < self.data:
            if self.left_node:
                self.left_node.insert(val)
                return
            self.left_node = BstAlgo(val)
            return
        if self.right_node:
            self.right_node.insert(val)
            return
        self.right_node = BstAlgo(val)

    def get_min(self):
        current = self
        while current.left_node is not None:
            current = current.left_node
        return current.data

    def get_max(self):
        current = self
        while current.right_node is not None:
            current = current.right_node
        return current.data

    def delete(self, val):
        if self is None:
            return self
        if val < self.data:
            self.left_node = self.left_node.delete(val)
            return self
        if val > self.data:
            self.right_node = self.right_node.delete(val)
            return self
        if self.right_node is None:
            return self.left_node
        if self.left_node is None:
            return self.right_node
        min_larger_node = self.right_node
        while min_larger_node.left:
            min_larger_node == min_larger_node.left
        self.data = min_larger_node.data
        self.right_node = self.right_node.delete(min_larger_node.data)

        return self

    def exists(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left_node is None:
                return False
            return self.left_node.exists(val)
        if self.right_node is None:
            return False
        return self.right_node.exists(val)

    def inorder(self, vals):
        if self.left_node is not None:
            self.left_node.inorder(vals)
        if self.data is not None:
            vals.append(self.data)
        if self.right_node is not None:
            self.right_node.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.data is not None:
            vals.append(self.data)
        if self.left_node is not None:
            self.left_node.preorder(vals)
        if self.right_node is not None:
            self.right_node.preorder(vals)

        return vals

    def postorder(self, vals):
        if self.left_node is not None:
            self.left_node.postorder(vals)
        if self.right_node is not None:
            self.right_node.postorder(vals)
        if self.data is not None:
            vals.append(self.data)
        return vals
