import pygame
from preguntas import *
from constantes import *


def crear_lista_paralela(key:str,lista:list):
    '''
Brief:
    Crea una lista paralela extrayendo un valor especifico (identificado por una clave) de cada diccionario en una lista de diccionarios.

Parametros:
    - key (str): La clave que se utilizara para extraer el valor de cada diccionario en la lista.
    - lista (list): La lista de diccionarios de la cual se extraeran los valores.

Retorno:
    lista_segun_key (list): Una nueva lista que contiene los valores extraidos de cada diccionario segun la clave especificada.
'''
    lista_segun_key = []
    for elemento in lista:
        lista_segun_key.append(elemento[key])
        
    return lista_segun_key


def renderizar_texto(texto:str,fuente:str,tamaño_fuente:int,color:tuple):
    '''
Brief:
    Renderiza un texto en una fuente, tamaño y color especificos utilizando la biblioteca Pygame.

Parametros:
    - texto (str): El texto que se desea renderizar.
    - fuente (str): El nombre de la fuente que se utilizara para renderizar el texto.
    - tamaño_fuente (int): El tamaño de la fuente para el texto.
    - color (tuple): Una tupla que representa el color para el texto.

Retorno:
    mensaje_renderizado: El texto renderizado como una superficie de Pygame.
'''
    fuente = pygame.font.SysFont(fuente,tamaño_fuente)
    mensaje = texto
    mensaje_renderizado = fuente.render(texto,True,color)

    return mensaje_renderizado



def determinar_perimetro_click( posicion_click:list,left:int,right:int,top:int,bottom:int):
    '''
Brief:
    Determina si un punto de clic esta dentro de un area definida por sus limites izquierdo, derecho, superior e inferior.

Parametros:
    - posicion_click (list): Una lista que contiene las coordenadas (x, y) del punto de clic que se desea verificar.
    - left (int): La coordenada x del limite izquierdo del area.
    - right (int): La coordenada x del limite derecho del area.
    - top (int): La coordenada y del limite superior del area.
    - bottom (int): La coordenada y del limite inferior del area.

Retorno:
    True si el punto de click esta dentro del area rectangular, False en caso contrario.
'''
    if (posicion_click[0] > left and posicion_click[0] < right) and (posicion_click[1] > top and posicion_click[1] < bottom):
        return True
    
    

    
def ocultar_opcion(opcion:dict):
    '''
    Brief:
        Oculta una opcion en un menu, reemplazando su texto renderizado por un espacio en blanco.

    Parametros:
        - opcion (dict): Un diccionario que representa una opcion del menu y contiene su texto renderizado.

    Retorno:
        Esta funcion no retorna ningun valor directamente, pero modifica la opcion proporcionada para ocultarla.
    '''
    opcion["texto_renderizado"] = renderizar_texto("","Arial",20,COLOR_GRIS)
    
    
def ocultar_opciones(opciones:dict):
    '''
    Brief:
        Oculta varias opciones en un menu, reemplazando sus textos renderizados por espacios en blanco.

    Parametros:
        - opciones (dict): Un diccionario que contiene multiples opciones de menu y sus textos renderizados.

    Retorno:
        Esta funcion no retorna ningun valor directamente, pero modifica las opciones proporcionadas para ocultarlas.
    '''
    for key in opciones:
        ocultar_opcion(opciones[key])
        

def cuadrado(pantalla):
    '''
    Brief:
        Dibuja un cuadrado en una superficie de pantalla.

    Parametros:
        - pantalla (pygame.Surface): La superficie de pantalla en la que se dibujaran los cuadrados.

    Retorno:
        Esta funcion no retorna ningun valor, ya que su objetivo es dibujar en la superficie proporcionada.
    '''
    pygame.draw.rect(pantalla,COLOR_ROJO,(18,15,210,110))  #Remarco boton pregunta
    pygame.draw.rect(pantalla,COLOR_AZUL,(23,20,200,100))  #Boton pregunta


def ocultar_o_mostrar_elementos(diccionario:dict,visibilidad:bool):
    '''
    Brief:
        Permite ocultar o mostrar elementos representados en un diccionario cambiando su propiedad de visibilidad.

    Parametros:
        - diccionario (dict): Un diccionario que contiene elementos con propiedades de visibilidad.
        - visibilidad (bool): Un valor booleano que determina si los elementos deben ser visibles (True) u ocultos (False).

    Retorno:
        Esta funcion no retorna ningun valor directamente, pero modifica el diccionario proporcionado para cambiar la visibilidad de sus elementos.
    '''
    for key in diccionario:
        diccionario[key]["visibilidad"] = visibilidad
        
        
        


  
