import json

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            ptr1 = self.root
            ptr2 = ptr1
            # find empty branch
            while ptr1 != None:
                ptr2 = ptr1
                if value <= ptr1.value:
                    ptr1 = ptr1.left
                else:
                    ptr1 = ptr1.right
            # assign node to empty branch
            if value <= ptr2.value:
                ptr2.left = newNode
            else:
                ptr2.right = newNode
        return self

    def lookup(self, value):
        ptr1 = self.root
        while ptr1 != None:
            if value < ptr1.value:
                ptr1 = ptr1.left
            elif value > ptr1.value:
                ptr1 = ptr1.right
            else:
                return True
        return False
    def remove(self, value):
        pass
    def print(self, node):
        while node != None:
            # root
            print(node.value)
            # left
            self.print(node.left)
            # right
            self.print(node.right)
            break
        return


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)

myTree.print(myTree.root)

print(myTree.lookup(4))
print(myTree.lookup(40))
# 9
# 4    20
# 1    6    15    170