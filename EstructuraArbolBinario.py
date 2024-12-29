"""
Author: Alain Gomez Zapata
Fecha: 26/12/2024
Nombre de Programa: Actividad 8 Estructura de Datos. Trabajo Final sobre Arboles Binarios.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecho, valor)

    def inorder(self):
        self._inorder_rec(self.raiz)

    def _inorder_rec(self, nodo):
        if nodo is not None:
            self._inorder_rec(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self._inorder_rec(nodo.derecho)

    def preorder(self):
        self._preorder_rec(self.raiz)

    def _preorder_rec(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self._preorder_rec(nodo.izquierdo)
            self._preorder_rec(nodo.derecho)

    def posorder(self):
        self._posorder_rec(self.raiz)

    def _posorder_rec(self, nodo):
        if nodo is not None:
            self._posorder_rec(nodo.izquierdo)
            self._posorder_rec(nodo.derecho)
            print(nodo.valor, end=' ')

# Main
arbol = ArbolBinario()
print("Ingrese los elementos para el árbol (separados por comas):")
elementos = list(map(int, input().split(',')))

for elem in elementos:
    arbol.insertar(elem)

print("Recorrido Inorder:")
arbol.inorder()
print("\nRecorrido Preorder:")
arbol.preorder()
print("\nRecorrido Posorder:")
arbol.posorder()