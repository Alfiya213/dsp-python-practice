# Aim: To simulate folder/file structure using Binary Tree.


# Node of Binary Tree
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Display the tree using Preorder Traversal
def display(root):
    if root is not None:
        print(root.name)
        display(root.left)
        display(root.right)


# Create folder/file structure
root = Node("Root")

root.left = Node("Documents")
root.right = Node("Pictures")

root.left.left = Node("Resume.pdf")
root.left.right = Node("Assignment.docx")

root.right.left = Node("Photo.jpg")
root.right.right = Node("Project.png")


# Display folder/file structure
print("Folder/File Structure:")
display(root)
