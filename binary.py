class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal of the BST:")
bst.inorder_traversal(bst.root)
print()
key = int(input('key:'))
if bst.search(key):
    print(f"\n{key} BST ichida topildi.")
else:
    print(f"\n{key} BST ichida topilmadi.")
