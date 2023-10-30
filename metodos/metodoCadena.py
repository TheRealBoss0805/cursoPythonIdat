cadena1= "Hola soy fer"
cadena2 = "calla webon"

print(dir(cadena1)) #(FUNCION) DEVUELVE LA LISTA DE LOS ATRIBUTOS VALIDOS DEL POBJETO PASADO
print(cadena1.upper()) #METODO QUE CONVIERTE EN MAYUSCULA
print(cadena1.lower()) #METODO QUE CONVIERTE EN MINUSCULA
print(cadena1.capitalize()) #METODO QUE CONVIERTE PRIMERA LETRA EN MAYUSCULA

busqueda_find = cadena1.find("Hola") #METODO QUE DEVUELVE LA POSICION DEL ELEMENTO EN LA CADENA SINO DEVUELVE -1
busqueda_find2 = cadena1.find("a")
busqueda_find3 = cadena1.find("v")

print(busqueda_find)
print(busqueda_find2)
print(busqueda_find3)

#busqueda_index = cadena1.index("v") #IGUAL QUE FIN PERO SI NO ENCUENTRA DEVUELVE UNA EXCEPCION
print(busqueda_index)
