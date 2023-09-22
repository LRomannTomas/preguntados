import pygame
from preguntas import *
from constantes import *
from funciones import *



#-------------------------------------------- SUBLISTAS------------------------------------------------------------#

lista_solo_preguntas = crear_lista_paralela("pregunta",lista_preguntas)
lista_opciones_a = crear_lista_paralela("a",lista_preguntas)
lista_opciones_b = crear_lista_paralela("b",lista_preguntas)
lista_opciones_c = crear_lista_paralela("c",lista_preguntas)
lista_opciones_correctas = crear_lista_paralela("correcta",lista_preguntas)


#----------------------------------------------SONIDOS-------------------------------------------------------------#

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("musica.mp3")
sonido_fondo.set_volume(0.2)
sonido_fondo.play()

sonido_error = pygame.mixer.Sound("sonido_error.wav")
sonido_acierto = pygame.mixer.Sound("sonido_acierto.mp3")
sonido_pregunta = pygame.mixer.Sound("sonido_pregunta.mp3")

#------------------------------------------------------------------------------------------------------------------#



#------------------------------------------PANTALLA E IMAGENES-----------------------------------------------------#

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("Preguntados") 


posicion_imagen = (325,5)
imagen = pygame.image.load("logo_preguntados.png")
imagen = pygame.transform.scale(imagen,(150,150))

background = pygame.image.load("back_wood.jpeg").convert()
background = pygame.transform.scale(background,(810,ALTO_VENTANA))

remarco = pygame.image.load("wood_white.jpg")
remarco = pygame.transform.scale(remarco,(208,107))

fondo_boton = pygame.image.load("wood_black.jpg")
fondo_boton = pygame.transform.scale(fondo_boton,(200,100))

corazon_vida_1 = pygame.image.load("corazon.png")
corazon_vida_1 = pygame.transform.scale(corazon_vida_1,(60,60))

corazon_vida_2 = pygame.image.load("corazon.png")
corazon_vida_2 = pygame.transform.scale(corazon_vida_2,(60,60))

#------------------------------------------------------------------------------------------------------------------#



#-----------------------------------------------VARIABLES----------------------------------------------------------#

fuente_1 = "Berlin_Sans_FB"
fuente_2 = "Segoe_UI_Black"

intentos = 0
indice = 0
puntos = 0 

#------------------------------------------------------------------------------------------------------------------#



opciones_y_pregunta_renderizadas = {
    "pregunta" : {"texto_renderizado" : renderizar_texto("",fuente_1,20,COLOR_ROJO), "posicion" : (180,170),
    "visibilidad" : True},
    
    "a" : {"texto_renderizado" : renderizar_texto("",fuente_2,20,COLOR_GRIS), "posicion" : (50,300),
    "visibilidad" : True},
    
    "b" : {"texto_renderizado" : renderizar_texto("",fuente_2,20,COLOR_GRIS),"posicion": (300,300),
    "visibilidad" : True},
    
    "c" : {"texto_renderizado" : renderizar_texto("",fuente_2,20,COLOR_GRIS),"posicion": (550,300),
    "visibilidad" : True},
    
    "mensaje final" : {"texto_renderizado" : renderizar_texto("",fuente_2,50,COLOR_GRIS),"posicion": (200,260),
    "visibilidad" : False} 
}

diccionario_paralelo = {
    "pregunta" : {"posicion": (23,20,200,100),"color": COLOR_AZUL},
    "a" : {"posicion": (35,265,230,100),"color": COLOR_AZUL},
    "b" : {"posicion": (285,265,230,100),"color": COLOR_AZUL},
    "c" : {"posicion": (535,265,230,100),"color": COLOR_AZUL},
    
    "mensaje final" : {"posicion" : (200,260),"color" : COLOR_AZUL}
}

        
     
etiquetas_y_puntuacion_renderizadas = {
    "etiqueta_pregunta": {"texto_renderizado" : renderizar_texto("PREGUNTA",fuente_1,20,COLOR_BLANCO) ,"posicion":(70,55),"visibilidad" : True},
    "etiqueta_reiniciar" : {"texto_renderizado" : renderizar_texto("REINICIAR",fuente_1,20,COLOR_BLANCO) ,"posicion":(630,55),"visibilidad" : True},
    "puntuacion" : {"texto_renderizado" : renderizar_texto(f"PUNTUACION ACTUAL: {puntos}",fuente_2,25,COLOR_GRIS),"posicion":(5,560),"visibilidad" : True},
    "mensaje final" : {"texto_renderizado" : renderizar_texto(f"PUNTAJE FINAL: {puntos}",fuente_1,50,COLOR_ROJO) ,"posicion":(200,260),"visibilidad" : True}
}



bandera_esta_jugando = False
bandera_abrio_juego = True


while bandera_abrio_juego:
    
    
    
    pantalla.fill(COLOR_BLANCO) #Se le pone un color de fondo a la ventana
    pantalla.blit(background,[0,0])
    pantalla.blit(imagen,posicion_imagen) 
    pantalla.blit(remarco,[569,17])
    pantalla.blit(fondo_boton,[573,20])
    pantalla.blit(remarco,[19,17])
    pantalla.blit(fondo_boton,[23,20])
    
    

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera_abrio_juego = False
        

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            
            
            
            perimetro_boton_pregunta = determinar_perimetro_click(posicion_click,18,228,15,125)
            perimetro_opcion_a = determinar_perimetro_click(posicion_click,35,265,265,365)
            perimetro_opcion_b = determinar_perimetro_click(posicion_click,285,515,265,365)
            perimetro_opcion_c = determinar_perimetro_click(posicion_click,535,765,265,365)
            perimetro_boton_reiniciar = determinar_perimetro_click(posicion_click,568,728,15,125)  
            
            if perimetro_boton_reiniciar:
                puntos = 0
                indice = 0
                intentos = 0
                etiquetas_y_puntuacion_renderizadas["puntuacion"]["texto_renderizado"] = renderizar_texto(f"PUNTUACION ACTUAL: {puntos}",fuente_2,25,COLOR_GRIS)
            
                
           
            
            if perimetro_boton_pregunta or perimetro_boton_reiniciar:
                
                sonido_pregunta.play()
                bandera_esta_jugando = True
                intentos = 0
                if indice < len(lista_opciones_correctas):
                    opciones_y_pregunta_renderizadas["pregunta"]["texto_renderizado"] = renderizar_texto(f"{indice + 1}) - {lista_solo_preguntas[indice]}",fuente_1,20,COLOR_BLANCO)
                    opciones_y_pregunta_renderizadas["a"]["texto_renderizado"] = renderizar_texto(f"A) {lista_opciones_a[indice]}",fuente_2,17,COLOR_BLANCO)
                    opciones_y_pregunta_renderizadas["b"]["texto_renderizado"] = renderizar_texto(f"B) {lista_opciones_b[indice]}",fuente_2,17,COLOR_BLANCO)
                    opciones_y_pregunta_renderizadas["c"]["texto_renderizado"] = renderizar_texto(f"C) {lista_opciones_c[indice]}",fuente_2,17,COLOR_BLANCO)
                    etiquetas_y_puntuacion_renderizadas["puntuacion"]["texto_renderizado"] = renderizar_texto(f"PUNTUACION ACTUAL: {puntos}",fuente_2,25,COLOR_GRIS)
                    
                
                                
                ocultar_o_mostrar_elementos(opciones_y_pregunta_renderizadas,True)
                opciones_y_pregunta_renderizadas["mensaje final"]["visibilidad"] = False
                
                if indice <= len(lista_opciones_correctas):    
                    indice += 1 
                
                
                
            if indice > len(lista_opciones_correctas):
                ocultar_o_mostrar_elementos(opciones_y_pregunta_renderizadas,False)
                
                opciones_y_pregunta_renderizadas["mensaje final"]["visibilidad"] = True
                etiquetas_y_puntuacion_renderizadas["mensaje final"]["texto_renderizado"] = renderizar_texto(f"PUNTAJE FINAL: {puntos}",fuente_1,50,COLOR_VERDE)
                etiquetas_y_puntuacion_renderizadas["puntuacion"]["texto_renderizado"] = renderizar_texto(f"",fuente_2,25,COLOR_GRIS)
                advertencia = renderizar_texto("ADVERTENCIA: al presionar el boton 'pregunta' comenzara el juego desde 0",fuente_1,20,COLOR_AMARILLO)
                
                indice = 0
                puntos = 0
                
            
            opcion_elegida = "" 
            if bandera_esta_jugando:
                
                if perimetro_opcion_a:
                    opcion_elegida = "a"
                elif perimetro_opcion_b:
                    opcion_elegida = "b"
                elif perimetro_opcion_c:
                    opcion_elegida = "c"
                
                    
                if opcion_elegida != "" and opciones_y_pregunta_renderizadas[opcion_elegida]["visibilidad"] == True:
                    if opcion_elegida == lista_preguntas[indice - 1]["correcta"] :
                        sonido_acierto.play()
                        puntos += 10
                        intentos = 0
                        bandera_esta_jugando = False
                    else:
                        intentos += 1    
                        sonido_error.play()
                        opciones_y_pregunta_renderizadas[opcion_elegida]["visibilidad"] = False
                    
                        if intentos == 2:    
                            intentos = 0              
                            bandera_esta_jugando = False
                    etiquetas_y_puntuacion_renderizadas["puntuacion"]["texto_renderizado"] = renderizar_texto(f"PUNTUACION ACTUAL: {puntos}",fuente_2,25,COLOR_GRIS)
                        
                
  
    if bandera_esta_jugando:
        
        for key in opciones_y_pregunta_renderizadas:
            
            if opciones_y_pregunta_renderizadas[key]["visibilidad"] == True and key != "mensaje final":
                
                pantalla.blit(fondo_boton,diccionario_paralelo[key]["posicion"])
                pantalla.blit(opciones_y_pregunta_renderizadas[key]["texto_renderizado"],opciones_y_pregunta_renderizadas[key]["posicion"])
                
                if intentos == 0:
                    pantalla.blit(corazon_vida_1,[700,530])
                    pantalla.blit(corazon_vida_2,[640,530])
                else:
                    if intentos == 1:
                        pantalla.blit(corazon_vida_2,[640,530])
                        
            else:
                if key == "mensaje final" and opciones_y_pregunta_renderizadas[key]["visibilidad"] == True:
                    
                    pantalla.blit(etiquetas_y_puntuacion_renderizadas["mensaje final"]["texto_renderizado"],etiquetas_y_puntuacion_renderizadas["mensaje final"]["posicion"])
                    pantalla.blit(advertencia,(100,200))
                    
                
    for key in etiquetas_y_puntuacion_renderizadas:
        if key != "mensaje final":
            pantalla.blit(etiquetas_y_puntuacion_renderizadas[key]["texto_renderizado"],etiquetas_y_puntuacion_renderizadas[key]["posicion"])
                    
                

    pygame.display.flip() #Aplica los cambios y los muestra en pantalla


pygame.quit() #Fin



