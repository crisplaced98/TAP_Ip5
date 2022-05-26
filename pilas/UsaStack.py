from pilas.ArrayStack import ArrayStack
from pilas.VectorStack import VectorStack
class UsaStack:
    def test(p):
        i = 0
        while not p.llena():
            p.push(10*i)
            i = i + 1
        while not p.vacia():
            print(p.pop())

    pila = ArrayStack(10)
    test(pila)

    pila = VectorStack(10)
    test(pila)

