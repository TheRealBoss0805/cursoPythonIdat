lista = ["Fernando", "Rivera", 1.71, 70]
print(lista[3])
print(lista)
tupla = ("Fernando", "Rivera", 1.71, 70)
tupla = ("THE BIGPIG")
print(tupla)
lista[3] = 25  # Si se puede modificar
#tupla[3] = 25  # No se puede modificar, para mostrarlo de igual manera va con corchetes
print(lista)

#CREANDO UN CONJUNTO (SET)
conjunto = {"Fernando", "Rivera", 1.71, True, 70} #no se puede ingresar por un índice
#tampoco se pueden repetir valores
#es necesario si o si un bucle para recorrer los elementos
#print(conjunto[3]) no es posible
conjunto = {"THE BOSS"}
print(conjunto)

#CREANDO UN DICCIONARIO (CLAVE Y VALOR COMO UN OBJETO EN JS)
diccionario = {
    'nombre': "Fernando Rivera",
    'altura': "1.70",
    'situacion': "Egresado",
    'apodo': "Chinano",
    'profesion': "Ingeniero"
}

diccionario2 = {
    0: "Fernando Rivera",
    1: "1.70",
    2: "Egresado",
    3: "Chinano",
    4: "Ingeniero"
}

diccionario3 = {
    "UNO": "FER",
    "DOS": "KATTY",
    "TRES": "JOSEPH",
    "CUATRO": "FRANK",
    "CINCO": "YOJES"
}


print("===================================================")
print(diccionario)
print(diccionario['apodo'])
print(diccionario2[4])
print(diccionario3)
print("===================================================")