
nombre_completo = "Tomas Roman"


nombre_completo.strip()  #Quita todos los espacios que se escuentren antes de que comienze el texto en un string. Ej: nombre = "   tomas"

nombre_completo.replace("Roman","Leonardo") #reemplaza el primer parametro que se encuentre en la cadena por el segundo

nombre_completo.split(" ") #crea una lista en la que se dividen los string por cada caracter que se ingrese por parametro

lista_nombres = nombre_completo.split(" ")

print(nombre_completo.count("m"))

"-".join(lista_nombres)  #junta los string mediante la cadena que se quiera





