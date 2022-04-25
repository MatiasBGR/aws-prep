from print_tree import printBTree

class TreeNode:

   def __init__(self,rootValue):
       self.info = rootValue
       self.left  = None
       self.right = None

   def printTree(self):
      printBTree(self,lambda n:(str(n.info),n.left,n.right)) 

class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root

    def add(self, info):
        if self.root is None:
            self.root = TreeNode(info)
        else:
            self._add(info, self.root)

    def _add(self, info, node):
        if info < node.info:
            if node.left is not None:
                self._add(info, node.left)
            else:
                node.left = TreeNode(info)
        else:
            if node.right is not None:
                self._add(info, node.right)
            else:
                node.right = TreeNode(info)

    def create(self, arr):
        if len(arr) > 0:
            for i in arr:
                self.add(i)

    def printTree(self):
        self.root.printTree()
   


def test ():
    tree = Tree()
    tree.create([3,1,7,5,4,23,65,7,33])
    tree.add(2)
    tree.printTree()


#test()