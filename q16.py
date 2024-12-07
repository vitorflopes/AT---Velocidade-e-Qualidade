class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def remove(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = remove(root.left, key)
    elif(key > root.data):
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = remove(root.right, temp.data)

    return root



# Testando o código (com os seus valores)
root = None
keys = [45, 25, 65, 20, 30, 60, 70]
for key in keys:
    root = insert(root, key)

print("Árvore em ordem (inicial):", end=" ")
inorder(root)
print()

root = remove(root, 20)
print("Árvore em ordem (após remover 20):", end=" ")
inorder(root)
print()

root = remove(root, 25)
print("Árvore em ordem (após remover 25):", end=" ")
inorder(root)
print()

root = remove(root, 45)
print("Árvore em ordem (após remover 45):", end=" ")
inorder(root)
print()

if search(root, 60):
  print("O valor 60 existe na árvore")