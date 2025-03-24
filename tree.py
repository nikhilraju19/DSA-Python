class Node:
    """
    This class contains the structure of a node in a binary tree.
    """
    def __init__(self, value):
        """
        Description:
            This function is a constructor to create a node.
        Parameters:
            self: self is the current reference object variable
            value: The value to store in the node.
        Return:
            None
        """
        self.left = None
        self.data = value
        self.right = None

class BinarySearchTree:
    """
    This class contains methods to create and traverse a binary search tree.
    """
    def __init__(self):
        """
        Description:
            This function is used to initialize the root node to none
        Parameters:
            self: self is the current reference object variable
        Return:
            None
        """
        self.root = None

    def insert(self, value):
        """
        Description:
            Inserts a value into the BST.
        Parameters:
            value: The value of the node that is being inserted into the tree
        Return:
            None
        """
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    current = current.left
                elif value > current.data:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    current = current.right
                elif value == current.data:
                    break

    def inorder(self, node):
        """
        Description:
            This function is used to traverse the tree in inorder format
        Parameters:
            self: self is the current object reference variable
            node: node is that node on which we are exploring
        Return:
            None
        """
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """
        Description:
            This function is used to traverse the tree in postorder format
        Parameters:
            self: self is the current object reference variable
            node: node is that node on which we are exploring
        Return:
            None
        """
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """
        Description:
            This function is used to traverse the tree in postorder format
        Parameters:
            self: self is the current object reference variable
            node: node is that node on which we are exploring
        Return:
            None
        """
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

def main():
    """
	Description:
		It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    tree = BinarySearchTree()
    elements = [25, 60, 15, 45, 79, 80, 33]
    for elem in elements:
        tree.insert(elem)

    print("Inorder Traversal of a binary tree is::", end=" ")
    tree.inorder(tree.root)
    print()

    print("Preorder Traversal:", end=" ")
    tree.preorder(tree.root)
    print()

    print("Postorder Traversal:", end=" ")
    tree.postorder(tree.root)
    print()


if __name__ == "__main__":
    main()