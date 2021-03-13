class procesar_archivo():

    #hacer la funcion que compare y que me devuelva un verdadero o falso
    def create_string(m, list):
        contador = 0
        list_aux = []
        ayuda = []

        for a in list:
            print("Dato: " + str(a._datos__dato))
            if int(m) < contador:
                ayuda.append(a._datos__dato)
                contador = contador + 1
            if contador == int(m):
                contador = 0
                list_aux.append(ayuda)
                ayuda.clear()


        for a in list_aux:
            print(a)