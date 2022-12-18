




print("Hola")
print("¿Que hay? ")
print("Vamos a aprender Python")
num_X = 5
num_Y = 10
num_Z = 20
resultado = num_X + num_Z - num_Y
print(resultado)










print("***Concatenacion***")

part1 = "Hola"
part2 = ", esta frase "
part3 = "esta formada por "
part4 = "tres concatenaciones"
print(part1 + part2 + part3 + part4)










print("***Asignacion***")

string1 = "Hola"
string1 += ", esta frase "
string1 += "esta formada por "
string1 += "tres asignaciones"
print(string1)











print("***Concatenar strings y valores numericos***")

num_X = 5
num_Y = 10
num_Z = 20
resultado = num_X + num_Z - num_Y
resultado = str(resultado)
print("El resultado es: " + resultado)













print("***Busqueda en un string***")

texto = "Encuentra a waldo"
buscar_subcadena = texto.find("waldo")
print(buscar_subcadena)













print("***Extraccion de una porcion del string***")

extraer_subcadena = texto[12:17]
print(extraer_subcadena)













print("***Comparacion***")

numero1 = 0
numero2 = 1
numero3 = 0

print(numero1 == numero2)
print(numero1 == numero3)










""" print("*FUNCIONES*")

def operacion(Numero1 , Numero2, Numero3):

    resultado=Numero1 + Numero2 + Numero3
    
    return resultado 

almacena_resultado=operacion(3,2.5,4)
print(almacena_resultado)

print(operacion(2,3,7))
print(operacion(1,1,1))
print(operacion(2,3.14,3))
print(operacion("t","e","xt"))
print(operacion(False, True, True)) """






# print("***LISTAS***")
""" lista=[1,2,4,5]
print(lista)

#Añadir elemento al final de la lista
lista.append(6)
print(lista)

#En el ".insert" se pone primero la posicion en la lista y luego el elemento a incluir
lista.insert(5,"Esto sobra")
print(lista)

#Eliminar elemento al final de la lista
lista.pop()
print(lista)

lista.insert(2,3)
print(lista)

lista.extend([7,8,9,10])
print(lista)

#Mostrar la posicion de un elemento
print(lista.index(7))

#Comprobar si un elemento se encuentra o no en una lista
print(5 in lista)
print(15 in lista)

#Las listas admiten todo tipo de datos
lista.extend(["texto",1,True,3.141592])
print(lista)

#Diferentes formas de llamar a una zona especifica de una lista
print(lista[:])
print(lista[:4])
print(lista[4:])
print(lista[9:13])
print(lista[13])

#El numero 1 se repite, si llamamos al indice del numero 1 nos va a dar la primera posicion con la que se encuentre en la lista.
print(lista.index(1))

#Borrar un elemento de la lista
lista.remove("texto")
print(lista)

#Concatenar varias lista
lista2=[11,12,13,14,15]
lista3=lista+lista2
print(lista3)
print(lista3)

#Multiplicar listas
lista4=["Hello"]*5
print(lista4)
#Tambien se puede multiplicar a la hora de imprimir
print(lista4*2) """

# print("***TUPLAS***")

#Las tuplas son listas inmutables que no admiten modificaciones
#Se puede extraer una porcion pero el resultado sera una nueva tupla
#Si permite comprobar si se encuentra o no un elemento en la lista
#Desde hace tiempo tambien se pueden hacer busquedas en el index, antes no se podia
#Ventajas sobre las listas:
#Mas ligeras y rapidas de ejecutar para el programa
#Permiten formatear strings
#Se pueden utilizar como claves de un diccionario

""" #Sintaxis-- nombre_tupla=(elem1,elem2,...) --Los parentesis son opcionales

tupla=("text",15,32,3.14)
#Acceder a un elemento concreto de la tupla
print(tupla[2])

#convertir una tupla en una lista y viceversa
listafromtupla=list(tupla)
tuplafromlista=tuple(listafromtupla)
print(listafromtupla)
print(tuplafromlista)
#Las listas van entre[] y las tuplas entre ()

#Buscar un elemento en la tupla
print(3.14 in tupla)
print(7 in tupla)

#Contar el nº de elementos que hay en una tupla
print(tupla.count(15))

#Saber la longitud de una tupla
print(len(tupla))

#Tupla unitaria, se debe poner una coma al final del elemento
tuplaunitaria=("elemento",)
print(tuplaunitaria)

#Desempaquetado de tuplas:
tupladesempaquetada=("Juan",15,1.12,True)
Nombre, Numero, Decimal, Booleano=tupladesempaquetada
print(Nombre)
print(Numero)
print(Decimal)
print(Booleano)"""


print("***DICCIONARIOS***")

#Estructura de datos similar a las listas y a las tuplas que permite almacenar varios valores de diferente tipo, incluso listas y otros diccionarios
#Los datos van asociados con el tipo de asociacion "clave:valor"
#Los datos no van ordenados ya que cada elemento esta asociado a una clave

""" diccionario={"Hard Rock":"Led Zeppelin", "Progresivo":"Pink Floyd","Grunge":"Nirvana","Rock Psicodelico":"Jefferson Airplane"}
print(diccionario)
print(diccionario["Progresivo"]) """


#Añadir dato al diccionario
""" diccionario["Punk Rock"]="Bad Bunny"
print(diccionario) """

#Para cambiar un valor solo hay que sobreescribir la clave ya existente

# diccionario["Punk Rock"]="Dead Kennedys
""" print(diccionario)
print(diccionario["Punk Rock"]) """

#No puede haber dos claves iguales por lo que siempre, si aparece la misma clave con diferente valor, esta sobreescribe a la anterior

#Eliminar un dato del diccionario
""" del diccionario["Grunge"]
print(diccionario) """

#Se pueden combinar todo tipo de datos 
""" diccionario2={"portero":1,True:3.14}
print(diccionario2)
print(diccionario2[True]) """

#Utilizar tuplas para asignar valores en el diccionario
""" tupla2=[1,2,3,4]
diccionario3={tupla2[0]:"uno",tupla2[1]:"dos",tupla2[2]:"tres",tupla2[3]:"cuatro"}
print(diccionario3)
print(diccionario3[2]) """

#Almacenar una tupla en un diccionario
""" diccionario4={"Nombre":"Iyan","Edad":23,"Dias de baja":[23,24,25,26,27]}
print(diccionario4)
print(diccionario4["Dias de baja"]) """

#Almacenar un diccionario con una tupla dentro de otro diccionario
""" diccionario4={"Nombre":"Iyan","Edad":24,"Dias de baja":[23,24,25,26,27],"Tratamientos":{"Fisicos":["Reahabilitacion","Estiramientos","Masajes"],"Medicacion":["Ibuprofeno","Paracetamol"]}}
print(diccionario4)
print(diccionario4["Tratamientos"]) """

#Obtener los valores del diccionario (Claves(.keys), Valores(.values) y Longitud(len(diccionario))
""" print(diccionario4.keys())
print(diccionario4.values())
print(len(diccionario4))"""



























'''print("**CONDICIONALES**")

#Condicional simple

def comprobar_horas_trabajadas(horas):
    resultado="No cumple minimos"
    if horas>7.45:
        resultado="Cumple minimos"
    return resultado

print(comprobar_horas_trabajadas(7.47))
print(comprobar_horas_trabajadas(7.32))

#Condicional con operador imput

horas_trabajadas=input("Introduzca las horas trabajadas: ")

def comprobar_horas_trabajadas(horas):
    resultado="No cumple minimos"
    if horas>7.45:
        resultado="Cumple minimos"
    return resultado

print(comprobar_horas_trabajadas(float(horas_trabajadas)))

#ejemplo anterior utilizando el operador "else" en el condicional if

horas_trabajadas=input("Introduzca las horas trabajadas: ")

def comprobar_horas_trabajadas(horas):   
    if horas>7.45:
        resultado="Cumple minimos"
    else:
        resultado="No cumple minimos"
    return resultado
print(comprobar_horas_trabajadas(float(horas_trabajadas)))

#El "else" siempre opera con el "if" mas cercano, ejemplo:
# def comprobar_horas_trabajadas(horas):   
#     if horas>7.45:                       <---- Este if no tiene ningun else asignado
#         resultado="Cumple minimos"
#     if horas>8.15:                       <----
#         resultado="Exceso de horas"          ]-- El "else" solo funciona con el if >8.15         
#     else:                                <----
#         resultado="No cumple minimos"
#     return resultado


#Operador "elif"

def comprobar_butaca():
    print("Comprobador de zona de asientos en el evento:")
    num_butaca=int(input("Introduzca el num. de butaca:"))
    if 0<num_butaca<=100:
        zona="FOSO"
    elif 100<num_butaca<=150:
        zona="TRIBUNA IZQ"
    elif 150<num_butaca<=200:
        zona="TRIBUNA DCHA"
    elif 200<num_butaca<=250:
        zona="TRIBUNA CENTRAL"
    else:  
        zona="ZONA RESERVADA"
    return "Su zona es:" + zona
    print("Disfrute del evento")
print(comprobar_butaca())
print(comprobar_butaca())
print(comprobar_butaca())
print(comprobar_butaca())
print(comprobar_butaca())
print(comprobar_butaca())
#En el ejemplo anterior se demuestra que se pueden utilizar varios operadores de comparacion dentro de un solo if '''