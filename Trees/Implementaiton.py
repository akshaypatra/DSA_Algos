class Node: 
    def __init__(self, key, parent=None): 
        self.key = key
        self.parent = parent 
        self.left = None
        self.right = None
        
        if parent is not None:
            if key < parent.key:
                assert(parent.left is None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else: 
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert(parent.right is None), 'parent already has a right child -- unable to create node'
                parent.right = self

    def get_leftmost_descendant(self):
        if self.left is not None:
            return self.left.get_leftmost_descendant()
        else:
            return self

    def search(self, key):
        if self.key == key: 
            return (True, self)
        elif key < self.key:
            if self.left:
                return self.left.search(key)
            else:
                return (False, self)
        else:
            if self.right:
                return self.right.search(key)
            else:
                return (False, self)

    def insert(self, key):
        found, node = self.search(key)
        if found:
            return None  # Key already exists
        else:
            # Insert new node as child of 'node'
            return Node(key, node)

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def delete(self, key):
        found, node_to_delete = self.search(key)
        assert found, f"key to be deleted:{key} does not exist in the tree"
        
        def transplant(node, new_child):
            if node.parent is None:
                pass  # This case depends on the context, assuming root here
            elif node == node.parent.left:
                node.parent.left = new_child
            else:
                node.parent.right = new_child
            if new_child:
                new_child.parent = node.parent

        # CASE 1
        if node_to_delete.left is None and node_to_delete.right is None:
            transplant(node_to_delete, None)
        
        # CASE 2
        elif node_to_delete.left is None:
            transplant(node_to_delete, node_to_delete.right)
        # CASE 3
        elif node_to_delete.right is None:
            transplant(node_to_delete, node_to_delete.left)
        
        # CASE 4
        else:
            successor = node_to_delete.right.get_leftmost_descendant()
            if successor.parent != node_to_delete:
                transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor
