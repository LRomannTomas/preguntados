import pygame
from preguntas import *
from constantes import *
from funciones import *

# A. Analizar detenidamente el set de datos.
# B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
# correcta.
# C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
# “Reiniciar”
# D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
# correctas. Cada respuesta correcta suma 10 puntos.
# E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
# siguiente pregunta.
# F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
# correcta, debe sumar el score y dejar de mostrar las opciones.
# G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
# opciones, deja de mostrar las opciones y no suma score
# H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
# También debe reiniciar el Score.


lista_solo_preguntas = crear_lista_paralela("pregunta",lista_preguntas)
lista_opciones_a = crear_lista_paralela("a",lista_preguntas)
lista_opciones_b = crear_lista_paralela("b",lista_preguntas)
lista_opciones_c = crear_lista_paralela("c",lista_preguntas)
lista_opciones_correctas = crear_lista_paralela("correcta",lista_preguntas)



pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) #Crea una pantalla con cierto tamaño
pygame.display.set_caption("Preguntados") #Titulo

posicion_imagen = (325,5)
posicion_pregunta = (180,170)
posicion_opcion_a = (50,300)
posicion_opcion_b = (300,300)
posicion_opcion_c = (550,300)
posicion_puntuacion = (5,560)
imagen = pygame.image.load("logo_preguntados.png")
imagen = pygame.transform.scale(imagen,(150,150))


fuente_1 = "Berlin_Sans_FB"
fuente_2 = "Segoe_UI_Black"
etiqueta_boton_pregunta = renderizar_texto("PREGUNTA",fuente_1,20,COLOR_ROJO)
etiqueta_boton_reiniciar = renderizar_texto("REINICIAR",fuente_1,20,COLOR_ROJO)
pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
puntuacion = renderizar_texto("",fuente_2,20,COLOR_GRIS)
puntos = 0
intentos = 0
indice = 0



bandera = True
while bandera:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        
        etiqueta_boton_pregunta = renderizar_texto("PREGUNTA",fuente_1,20,COLOR_ROJO)
        etiqueta_boton_reiniciar = renderizar_texto("REINICIAR",fuente_1,20,COLOR_ROJO)
        puntuacion = renderizar_texto(f"PUNTUACION ACTUAL: {puntos}",fuente_2,25,COLOR_GRIS)
        
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            
            
            perimetro_boton_pregunta = determinar_perimetro_click(posicion_click,18,228,15,125)
            perimetro_opcion_a = determinar_perimetro_click(posicion_click,35,265,265,365)
            perimetro_opcion_b = determinar_perimetro_click(posicion_click,285,515,265,365)
            perimetro_opcion_c = determinar_perimetro_click(posicion_click,535,765,265,365)
            
                
            if  perimetro_boton_pregunta == True:
                pregunta = renderizar_texto(f"{indice + 1}) - {lista_solo_preguntas[indice]}",fuente_1,20,COLOR_ROJO)
                opcion_a = renderizar_texto(f"A) {lista_opciones_a[indice]}",fuente_2,20,COLOR_GRIS)
                opcion_b = renderizar_texto(f"B) {lista_opciones_b[indice]}",fuente_2,20,COLOR_GRIS)
                opcion_c = renderizar_texto(f"C) {lista_opciones_c[indice]}",fuente_2,20,COLOR_GRIS)
                indice += 1
                
            if indice == len(lista_opciones_correctas):
                indice = 0
                
            
            if indice >= 0:          
                if perimetro_opcion_a == True:
                    opcion_elegida = "a"
                    if opcion_elegida == lista_preguntas[indice - 1]["correcta"]:
                        puntos += 10
                        pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                        opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                        opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                        opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                        intentos = 0
                    else:
                        intentos += 1
                    if intentos == 2 :    
                        pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                        opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                        opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)       #preguntar como puedo no repetir codigo en esta parte - ya que las funciones no le reasignan un valor nuevo a una variable, (cuando asigno un parametro lo que pasa es que se crea una varibale interna), con las variables no puedo modificar una variable local
                        opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                        intentos = 0                        
                else:
                    if perimetro_opcion_b == True:
                        opcion_elegida = "b"
                        if opcion_elegida == lista_preguntas[indice - 1]["correcta"]:
                            puntos += 10
                            pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                            opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                            opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                            opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                            intentos = 0
                        else:
                            intentos += 1
                        if intentos == 2:
                                pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                                opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                intentos = 0
                    else:
                        if perimetro_opcion_c == True:
                            opcion_elegida = "c"
                            if opcion_elegida == lista_preguntas[indice - 1]["correcta"]:
                                puntos += 10
                                pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                                opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                intentos = 0
                            else:
                                intentos += 1
                            if intentos == 2:
                                pregunta = renderizar_texto("",fuente_1,20,COLOR_ROJO)
                                opcion_a = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_b = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                opcion_c = renderizar_texto("",fuente_2,20,COLOR_GRIS)
                                intentos = 0
                print(intentos)
                            
                                
                                
# G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
# opciones, deja de mostrar las opciones y no suma score                
                
            
            
    
            
    
    pantalla.fill(COLOR_BLANCO) #Se le pone un color de fondo a la ventana
    pantalla.blit(imagen,posicion_imagen) #Funde la imagen en la superficie pantalla
    pantalla.blit(pregunta,posicion_pregunta)
    
    
    pygame.draw.rect(pantalla,COLOR_AZUL,(35,265,230,100))  #Boton Opcion A 
    pygame.draw.rect(pantalla,COLOR_AZUL,(285,265,230,100)) #Boton Opcion B                                 
    pygame.draw.rect(pantalla,COLOR_AZUL,(535,265,230,100)) #Boton Opcion C 
    
    
    
    pantalla.blit(opcion_a,posicion_opcion_a)
    pantalla.blit(opcion_b,posicion_opcion_b)
    pantalla.blit(opcion_c,posicion_opcion_c)
    pantalla.blit(puntuacion,posicion_puntuacion)
    
    pygame.draw.rect(pantalla,COLOR_ROJO,(18,15,210,110))  #Remarco boton pregunta
    pygame.draw.rect(pantalla,COLOR_AZUL,(23,20,200,100))  #Boton pregunta
    pygame.draw.rect(pantalla,COLOR_ROJO,(568,15,210,110)) #Remarco boton reiniciar
    pygame.draw.rect(pantalla,COLOR_AZUL,(573,20,200,100)) #Boton reiniciar
    
    
  
    
    
    pantalla.blit(etiqueta_boton_pregunta,(70,55))
    pantalla.blit(etiqueta_boton_reiniciar,(630,55))
    pygame.display.flip() #Aplica los cambios y los muestra en pantalla
   

pygame.quit() #Fin












