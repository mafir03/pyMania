class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def adoptChild(self, child):
        child = Node(child)
        self.root.children.append(child)

    def printLeaf(self):
        for child in self.root.children:
            print(child.data)

def main():
    singleTree = Tree(10)
    singleTree.adoptChild()
if __name__ == '__main__':

