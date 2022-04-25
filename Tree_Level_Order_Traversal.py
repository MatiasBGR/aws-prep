from binary_tree import Tree
from Tree_Height_of_a_Binary_Tree import height

def levelOrder(root):
    if not root: return
    lista =  [root] #FIFO
    while (lista):
        nodo = lista.pop(0)
        print (nodo.info, end=' ')
        if nodo.left: lista.append(nodo.left)
        if nodo.right: lista.append(nodo.right)

'''
ruteo 01
1
 \
  2
   \
    5
   / \
  3   6
   \
    4

cola
[1]
-> sacamos el primer elemento de la cola: nodo = 1, cola = [ ]
-> imprimimos su valor: print (1, end=' ')
impresion = 1
-> no tiene hijo izquierdo: nodo = 1, cola = [ ]
-> si tiene hijo derecho: nodo = 1, cola = [ ]
-> sacamos el primer elemento de la cola: nodo = 2, cola = [ ]
-> imprimimos su valor: print (2, end=' ')
impresion = 1, 2
-> no tiene hijo izquierdo: nodo = 2, cola = [ ]
-> si tiene hijo derecho: nodo = 2, cola = [ 5 ]
-> sacamos el primer elemento de la cola: nodo = 5, cola = [ ]
-> imprimimos su valor: print (5, end=' ')
impresion = 1, 2, 5
-> si tiene hijo izquierdo: nodo = 5, cola = [ 3 ]
-> si tiene hijo derecho: nodo = 5, cola = [ 3, 6 ]
-> sacamos el primer elemento de la cola: nodo = 3, cola = [ 6 ]
-> imprimimos su valor: print (3, end=' ')
impresion = 1, 2, 5, 3
-> no tiene hijo izquierdo: nodo = 3, cola = [ 6 ]
-> si tiene hijo derecho: nodo = 3, cola = [ 6, 4 ]
-> sacamos el primer elemento de la cola: nodo = 6, cola = [ 4 ]
-> imprimimos su valor: print (6, end=' ')
impresion = 1, 2, 5, 3, 6
-> no tiene hijo izquierdo: nodo = 6, cola = [ 4 ]
-> no tiene hijo derecho: nodo = 6, cola = [ 4 ]
-> sacamos el primer elemento de la cola: nodo = 4, cola = [ ]
-> imprimimos su valor: print (4, end=' ')
impresion = 1, 2, 5, 3, 6, 4
while termina, lista vacia
'''


'''
ruteo 02
      4
   __/ \_
  2      7
 / \    / \
1   3  5   8
        \
         6
4 2 7 1 3 5 8 6 %
cola
[4]
-> sacamos el primer elemento de la cola: nodo = 4, cola = [ ]
-> imprimimos su valor: print (4, end=' ')
impresion = 4
-> si tiene hijo izquierdo: nodo = 4, cola = [ 2 ]
-> si tiene hijo derecho: nodo = 4, cola = [ 2, 7 ]
-> sacamos el primer elemento de la cola: nodo = 2, cola = [ 7 ]
-> imprimimos su valor: print (2, end=' ')
impresion = 4, 2
-> si tiene hijo izquierdo: nodo = 2, cola = [ 7, 1 ]
-> si tiene hijo derecho: nodo = 2, cola = [ 7, 1, 3 ]
-> sacamos el primer elemento de la cola: nodo = 7, cola = [ 1, 3 ]
-> imprimimos su valor: print (7, end=' ')
impresion = 4, 2, 7
-> si tiene hijo izquierdo: nodo = 7, cola = [ 1, 3, 5 ]
-> si tiene hijo derecho: nodo = 7, cola = [ 1, 3, 5, 8 ]
-> sacamos el primer elemento de la cola: nodo = 1, cola = [ 3, 5, 8 ]
-> imprimimos su valor: print (1, end=' ')
impresion = 4, 2, 7, 1
-> no tiene hijo izquierdo: nodo = 1, cola = [ 3, 5, 8 ]
-> no tiene hijo derecho: nodo = 1, cola = [ 3, 5, 8 ]
-> sacamos el primer elemento de la cola: nodo = 3, cola = [ 5, 8 ]
-> imprimimos su valor: print (3, end=' ')
impresion = 4, 2, 7, 1, 3
-> no tiene hijo izquierdo: nodo = 3, cola = [ 5, 8 ]
-> no tiene hijo derecho: nodo = 3, cola = [ 5, 8 ]
-> sacamos el primer elemento de la cola: nodo = 5, cola = [ 8 ]
-> imprimimos su valor: print (5, end=' ')
impresion = 4, 2, 7, 1, 3, 5
-> no tiene hijo izquierdo: nodo = 5, cola = [ 8 ]
-> si tiene hijo derecho: nodo = 5, cola = [ 8, 6 ]
-> sacamos el primer elemento de la cola: nodo = 8, cola = [ 6 ]
-> imprimimos su valor: print (8, end=' ')
impresion = 4, 2, 7, 1, 3, 5, 8
-> no tiene hijo izquierdo: nodo = 8, cola = [ 6 ]
-> no tiene hijo derecho: nodo = 8, cola = [ 6 ]
-> sacamos el primer elemento de la cola: nodo = 6, cola = [ ]
-> imprimimos su valor: print (6, end=' ')
impresion = 4, 2, 7, 1, 3, 5, 8, 6
while termina, lista vacia

'''
def test():
    tree01 = Tree()
    tree02 = Tree()


    tree01.create([1,2,5,3,6,4])
    tree02.create([4,7,2,1,5,6,8,3])

    tree01.printTree()
    levelOrder(tree01.root)
    
    print('############################################')
    print()

    tree02.printTree()
    levelOrder(tree02.root)