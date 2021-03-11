from listaDoblementeEnlazada import listaCircular
from gravphiz import gravphiz as grafica
from procesar_archivo import procesar_archivo as pa
import xml.etree.ElementTree as ET
from tkinter import filedialog
from matrices import matrices
from datos import datos
from time import sleep

list = listaCircular()
indice = 0

def datos_estudiante():
        print("Kevyn Josué Girón Jiménez")
        print("201700653")
        print("Introduccion a la Programacion y Computacion 2 seccion 'A' ")
        print("Ingenieria en Ciencias y Sistemas")
        print("4to Semestre")

def bi(dato):
    if(dato == 0):
        return 0
    else:
       return 1

def cargar_archivo():
    global indice
    archivo = filedialog.askopenfilename(title = "abrir")
    xml_doc = ET.parse(archivo)
    raiz = xml_doc.getroot()
    print("Cargando archivo")
    sleep(1)
    for hijo in raiz:
        indice = indice + 1
        print(indice)
        list_aux = []
        nombre = hijo.attrib["nombre"]
        n = hijo.attrib["n"]
        m = hijo.attrib["m"]
        print("Cargando datos")
        sleep(1)
        for a in hijo:
            text = int(a.text)
            x = a.attrib["x"]
            y = a.attrib["y"]
            list_aux.append(datos(text, x, y, bi(text)))
        list.push(matrices(nombre, n, m, indice, list_aux))
    print("Listo")
    #list.print()
    #list.search(1)
    #print(list.graphviz_code())

def main():
    
    while(True):
        print("--------------------Menu--------------------")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos estudiante")
        print("5. Generar Grafica")
        print("6. Salida")

        selec = input()

        if(selec == "1"):
            cargar_archivo()
            #datos_estudiante()
            #list = listaDoblementeEnlazada()

            #list.agregar_final(10)
            #list.agregar_final(20)
            #list.agregar_final(30)
            #list.agregar_final(40)
            #list.agregar_final(50)
            #list.print()
        elif(selec == "2"):
            print("")
        elif(selec == "3"):
            print("")
        elif(selec == "4"):
            datos_estudiante()
        elif(selec == "5"):
            code = ""
            print("0. Lista Circular")
            list.print()
            print("Selecciona una opcion...")
            x = input()
            if x == "0":
                code = grafica.circular_code(list.graphviz_code())
            else:
                code = list.search(x)
            grafica.create_file(code)
            grafica.compilar_dot()
            #print(list.graphviz_code())
        elif(selec == "6"):
            break
        else:
            print("No se ha seleccionado ninguna opcion correcta")

main()
