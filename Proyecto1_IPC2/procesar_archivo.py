class procesar_archivo():

    #hacer la funcion que compare y que me devuelva un verdadero o falso
    def crear_lista(datos, m):

        list = []
        sublist = []

        for a in datos:
            sublist.append(a)
            
            if int(a._datos__y) % m == 0:
                list.append(sublist)
                sublist = []

        tamaño = len(list)