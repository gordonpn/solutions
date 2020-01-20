# Write a function to traverse a binary search tree using inorder traversal.

class Node:
    def __init__(self, data):
        self.left: Node = None
        self.right: Node = None
        self.data = data

    def insert_bst(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif self.data <= data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def inorder(self):
        if self.data:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()