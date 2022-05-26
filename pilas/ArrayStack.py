from pilas.Stack import Stack


class ArrayStack(Stack):
    def __init__(self, tam):
        self.__monton = [None] * tam
        self.__cima = 0

    def push(self, elem):
        self.__monton[self.__cima] = elem
        self.__cima = self.__cima + 1

    def pop(self):
        self.__cima = self.__cima - 1
        return self.__monton[self.__cima]

    def llena(self):
        return self.__cima == len(self.__monton)

    def vacia(self):
        return self.__cima == 0

    @property
    def cima(self):
        return self.__cima
