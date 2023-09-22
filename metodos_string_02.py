import re
#se importa ReGex para poder utilizar sus funciones.


texto_1 = "1 uno 2 dos 3 tres 4 cuatro"
texto_1 = re.split("[0-9]+",texto_1)        #el primer parametro sera el separador y el segundo el texto que quiero evaluar
print(texto_1)

texto_2 = "1 uno 2 dos 3 tres 4 cuatro"
texto_2 =re.findall("[0-9]+",texto_2)    #encuentra especificamente lo que se le pasa por parametro
print(texto_2)

texto_3 = "a b  c"
texto_3 = re.sub(" ","_",texto_3)        #reemplaza cada coincidencia con el primer parametro con lo que se le haya pasado en el segundo
print(texto_3)

'''
Codigos escapados:
\d numericos
\D no numericos
\s espacios en blanco
\S no espacio en blanco
\w alfanumericos
\W no alfanumericos

'''

'''un ejemplo de uso para utilizar el codigo escapado puede ser el siguiente'''

texto_4 = "a b  c"
texto_4 = re.sub(r"\s+","_",texto_4)        #a diferencia del ejemplo anterior, se muestra diferente!
print(texto_4)



texto_5 = "QUEVEDO || BZRP MUSIC SESSIONS #52"
#lista_1 = re.split("[\|#]+",texto_5)

lista = re.split(r"\W+",texto_5,1)


# artista = lista_1[0]
# tipo = lista_1[1]
# numero = lista_1[2]
print(lista)
