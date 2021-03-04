class matrices:
    """description of class"""

    def __init__(self, nombre, n, m, indice, lista = []):
        self.__nombre = nombre
        self.__n = n
        self.__m = m
        self.__lista = lista
        self.__indice = indice

    @property
    def nombre(self):
        return self.__nombre

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def lista(self):
        return self.__lista

    @property
    def indice(self):
        return self.__indice

    def nombre(self, valor):
        self.__nombre = valor

    def n(self, valor):
        self.__n = valor

    def m(self, valor):
        self.__m = valor

    def m(self, valor):
        self.__lista = valor

    def indice(self, valor):
        self.__indice = valor
