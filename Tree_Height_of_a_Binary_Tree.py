#Tree: Height of a Binary Tree

from binary_tree import Tree


def height(root):
    if not root: return 0
    right = height(root.right) + 1 if root.right else 0
    left = height(root.left) + 1 if root.left else 0
    return right if right > left else left

def test():
    tree01 = Tree()
    tree02 = Tree()
    tree03 = Tree()

    tree01.create([3,5,2,1,4,6,7])
    tree02.create([15])
    tree03.create([3,1,7,5,4])

    tree01.printTree()
    print (height(tree01.root))
    print('############################################')
    print()
    tree02.printTree()
    print (height(tree02.root))
    print('############################################')
    print()
    tree03.printTree()
    print (height(tree03.root))