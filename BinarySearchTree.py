class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, item):
    if root is None:
        return Node(item)

    if item < root.data:
        root.left = insert(root.left, item)
    else:
        root.right = insert(root.right, item)
    
    return root

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

def PreOrder(root):
    if root:
        print(root.data, end=" ")
        PreOrder(root.left)
        PreOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=" ")

root = None

num = [1,2,4,8,5,9,6,3,1,88,33,44,55,3,4,56,85,40,75]
for elm in num:
    root = insert(root, elm)

def find_height(node):
    if node is None:
        return -1
   
    left_height = find_height(node.left)
    right_height = find_height(node.right)
   
    return max(left_height, right_height) + 1

def search(root, key):
    # Base case: root is None or key is present at root
    if root is None:
        return False
    if root.data == key:
        return True

    # Key is greater than root's data
    if key > root.data:
        return search(root.right, key)
    
    # Key is smaller than root's data
    return search(root.left, key)

print("In Order:",end=" ")
InOrder(root) # In-order Traversal
print()

print("Pre Order:",end=" ")
PreOrder(root) # Per-order Traversal
print()

print("Post Order:",end=" ")
PostOrder(root) # Post-order Traversal
print()

print("Height =",find_height(root))