class Tree:
    def __init__(self):
        self.root=None
    
    def postorder(self):
        node = self.root
        data = []

        def recursion(node):
           if not node:
               return
           # left right root
           recursion(node.left)
           recursion(node.right)
           if node.data not in data:
               data.append(node.data)
        recursion(node)
        return data

class Node:
    def __init__(self , data):
        self.data =data
        self.left = None
        self.right = None
        # self.children = []


if __name__ == '__main__':
    
    tree = Tree()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    tree.root = n1

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n3.left = n6

    n4.left= n7

    treeData = tree.postorder()

    print(treeData)
