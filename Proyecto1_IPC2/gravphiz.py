import os

class gravphiz():
    """description of class"""

    def create_string(name, n, m, list):
        eme = '"m = ' + m + '"'
        ene = '"n = ' + n + '"'
        head = 'digraph mat{\nrankdir=UD\n\tMatrices->' + name + '\n'
        body = '\t' + name + '->' + eme + '\n\t' + name + '->' + ene + '\n'
        declarar_nodos = ""
        contador = 0
        body_aux = ""
        list_aux = []
        ayuda = []
        code = ""
        #str(a._datos__dato)
        cont = 0
        for a in list:
            declarar_nodos = declarar_nodos + '"n' + str(cont) + '" [label = "' + str(a._datos__dato) + '"]\n'
            cont = cont + 1

        #for a in ayuda:
         #   print(a)

        cont_aux = 0
        for a in list:
            if contador < int(m):
                body_aux = body_aux + '->n' + str(cont_aux) #str(a._datos__dato)
                contador = contador + 1
            #print(a._datos__dato)
            if contador == int(m):
                list_aux.append(body_aux)
                body_aux = ""
                contador = 0
            cont_aux = cont_aux + 1
        #print(list_aux)
        for a in list_aux:
            body_aux = body_aux + '\t' + name + a + '\n'
            
        code = head + declarar_nodos + body + body_aux + '\n}'
        #print(code)
        return code

    def circular_code(cadena):
        code = 'digraph mat{\nrankdir=UD\n' + cadena + '\n}'
        return code

    def create_file(cadena):

        f = open("archivo.dot", "w")
        f.write(cadena)
        f.closed

    def compilar_dot():
        os.system('dot -Tjpg archivo.dot -o Imagen.jpg')
        os.system("Imagen.jpg")