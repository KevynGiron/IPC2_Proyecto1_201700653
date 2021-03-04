from nodoCircular import nodoCircular as nodo
from procesar_archivo import procesar_archivo as proceso

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
        aux = self.head
        while (aux.next != self.head):
            #print(aux.data._matrices__nombre) #imprimir datos de la matriz
            if value == aux.data._matrices__indice:
                li = aux.data._matrices__lista
                proceso.crear_lista(li, int(aux.data._matrices__m))
                break
            #for a in li:
                #print(a._datos__dato)
                #print(a._datos__binario)
                #print(a._datos__x)
                #print(a._datos__y)
            aux = aux.next
        #print(aux.data._matrices__nombre)
        if value == aux.data._matrices__indice:
                li = aux.data._matrices__lista
                proceso.crear_lista(li, int(aux.data._matrices__m))
        #li = aux.data._matrices__lista
        #for a in li:
            #print(a._datos__dato)
            #print(a._datos__binario)
            #print(a._datos__x)
            #print(a._datos__y)

    def graphviz_code(self):
        code = ""
        aux = self.head
        code2 = ""

        if self.is_empty():
            code = '\t"Esta vacia"'
        else:
            code2 = aux.next.data._matrices__nombre
            while (aux.next != self.head):
                code2 = aux.next.data._matrices__nombre
                code = code + '\t"' + aux.data._matrices__nombre + '"-->"' + '"' + code2 + '"\n'
                aux = aux.next
            code = code + '\t"' + code2 + '"-->' + '"' + self.head.data._matrices__nombre + '"' +'"\n'
        return code
