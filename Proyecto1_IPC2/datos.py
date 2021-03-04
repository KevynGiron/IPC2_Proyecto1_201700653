class datos():
    """description of class"""
    def __init__(self, dato, x, y, binario):
        self.__dato = dato
        self.__x = x
        self.__y = y
        self.__binario = binario

    @property
    def dato(self):
        return self.__dato

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def binario(self):
        return self.__binario

    def dato(self, valor):
        self.__dato = valor

    def x(self, valor):
        self.__x = valor

    def y(self, valor):
        self.__y = valor

    def binario(self, valor):
        self.__binario = valor
