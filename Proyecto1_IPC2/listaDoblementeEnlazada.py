from nodoCircular import nodoCircular as nodo
from procesar_archivo import procesar_archivo as pro
from gravphiz import gravphiz as proceso

class listaCircular():

    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None

    def push(self, dato):
        if self.is_empty():
            self.head = self.tail = nodo(dato)
            self.tail.next = self.head
        else:
            aux = self.tail
            self.tail = aux.next = nodo(dato)
            self.tail.next = self.head 

    def print(self):
        aux = self.head
        while (aux.next != self.head):
            print(str(aux.data._matrices__indice) + ". " + aux.data._matrices__nombre) #imprimir datos de la matriz
            #li = aux.data._matrices__lista
            #for a in li:
                #print(a._datos__dato)
                #print(a._datos__binario)
                #print(a._datos__x)
                #print(a._datos__y)
            aux = aux.next
        print(str(aux.data._matrices__indice) + ". " + aux.data._matrices__nombre)
        #li = aux.data._matrices__lista
        #for a in li:
            #print(a._datos__dato)
            #print(a._datos__binario)
            #print(a._datos__x)
            #print(a._datos__y)

    def search(self, value):
        code = ""
        aux = self.head
        while (aux.next != self.head):
            #print(aux.data._matrices__nombre) #imprimir datos de la matriz
            if value == aux.data._matrices__indice:
                li = aux.data._matrices__lista
                code = proceso.create_string(aux.data._matrices__nombre, aux.data._matrices__m, aux.data._matrices__n, li)
                break

            aux = aux.next
        #---------------------------------------------------------------------------------
        if value == aux.data._matrices__indice:
            li = aux.data._matrices__lista
            code = proceso.create_string(aux.data._matrices__nombre, aux.data._matrices__m, aux.data._matrices__n, li)
        #-------------------------------------------------------------------------
        print(code)
        return code

    def process(self, value):
        aux = self.head
        while (aux.next != self.head):
            #print(aux.data._matrices__nombre) #imprimir datos de la matriz
            if value == aux.data._matrices__indice:
                li = aux.data._matrices__lista
                pro.create_string(aux.data._matrices__n, li)
                break
            aux = aux.next
        #---------------------------------------------------------------------------------
        if value == aux.data._matrices__indice:
            li = aux.data._matrices__lista
            pro.create_string(aux.data._matrices__m, li)
        #-------------------------------------------------------------------------
        
    def graphviz_code(self):
        code = ""
        aux = self.head
        code2 = ""
        lista = []

        if self.is_empty():
            code = '\t"Esta vacia"'
        else:
            #code2 = aux.next.data._matrices__nombre
            lista.append(aux.data._matrices__nombre)
            while (aux.next != self.head):
                lista.append(aux.next.data._matrices__nombre)
                #code2 = aux.next.data._matrices__nombre
                #code = code + '\t"' + aux.data._matrices__nombre + '"->"' + code2 + '"\n'
                aux = aux.next
            #code = code + '\t"' + code2 + '"->' + self.head.data._matrices__nombre + '"' +'"\n'
        declarar_nodos = ""
        cont = 0
        for a in lista:
            declarar_nodos = declarar_nodos + '"n' + str(cont) + '" [label = "' + str(a) + '"]\n'
            cont = cont + 1
        contador = 0
        for a in lista:
            code = code + 'n' + str(contador) + '->'
            contador = contador + 1
        code = code + 'n0'
        final_code = declarar_nodos + code
        return final_code
