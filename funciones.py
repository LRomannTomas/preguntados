import pygame
from preguntas import *
from constantes import *


def crear_lista_paralela(key:str,lista:list):
    '''
Brief:
    Crea una lista paralela extrayendo un valor específico (identificado por una clave) de cada diccionario en una lista de diccionarios.

Parámetros:
    - key (str): La clave que se utilizará para extraer el valor de cada diccionario en la lista.
    - lista (list): La lista de diccionarios de la cual se extraerán los valores.

Retorno:
    lista_segun_key (list): Una nueva lista que contiene los valores extraídos de cada diccionario según la clave especificada.
'''
    lista_segun_key = []
    for elemento in lista:
        lista_segun_key.append(elemento[key])
        
    return lista_segun_key


def renderizar_texto(texto:str,fuente:str,tamaño_fuente:int,color:tuple):
    '''
Brief:
    Renderiza un texto en una fuente, tamaño y color específicos utilizando la biblioteca Pygame.

Parámetros:
    - texto (str): El texto que se desea renderizar.
    - fuente (str): El nombre de la fuente que se utilizará para renderizar el texto.
    - tamaño_fuente (int): El tamaño de la fuente para el texto.
    - color (tuple): Un tuple que representa el color en formato RGB (Red, Green, Blue) para el texto.

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
    Determina si un punto de clic está dentro de un area definida por sus límites izquierdo, derecho, superior e inferior.

Parámetros:
    - posicion_click (list): Una lista que contiene las coordenadas (x, y) del punto de clic que se desea verificar.
    - left (int): La coordenada x del límite izquierdo del área.
    - right (int): La coordenada x del límite derecho del área.
    - top (int): La coordenada y del límite superior del área.
    - bottom (int): La coordenada y del límite inferior del área.

Retorno:
    True si el punto de clic está dentro del área rectangular, False en caso contrario.
'''
    if (posicion_click[0] > left and posicion_click[0] < right) and (posicion_click[1] > top and posicion_click[1] < bottom):
        return True
    
    

    
def ocultar_opcion(opcion:dict):
    '''
    Brief:
        Oculta una opción en un menú, reemplazando su texto renderizado por un espacio en blanco.

    Parámetros:
        - opcion (dict): Un diccionario que representa una opción del menú y contiene su texto renderizado.

    Retorno:
        Esta función no retorna ningún valor directamente, pero modifica la opción proporcionada para ocultarla.
    '''
    opcion["texto_renderizado"] = renderizar_texto("","Arial",20,COLOR_GRIS)
    
    
def ocultar_opciones(opciones:dict):
    '''
    Brief:
        Oculta varias opciones en un menú, reemplazando sus textos renderizados por espacios en blanco.

    Parámetros:
        - opciones (dict): Un diccionario que contiene múltiples opciones de menú y sus textos renderizados.

    Retorno:
        Esta función no retorna ningún valor directamente, pero modifica las opciones proporcionadas para ocultarlas.
    '''
    for key in opciones:
        ocultar_opcion(opciones[key])
        

def cuadrado(pantalla):
    '''
    Brief:
        Dibuja un cuadrado en una superficie de pantalla.

    Parámetros:
        - pantalla (pygame.Surface): La superficie de pantalla en la que se dibujarán los cuadrados.

    Retorno:
        Esta función no retorna ningún valor, ya que su objetivo es dibujar en la superficie proporcionada.
    '''
    pygame.draw.rect(pantalla,COLOR_ROJO,(18,15,210,110))  #Remarco boton pregunta
    pygame.draw.rect(pantalla,COLOR_AZUL,(23,20,200,100))  #Boton pregunta


def ocultar_o_mostrar_elementos(diccionario:dict,visibilidad:bool):
    '''
    Brief:
        Permite ocultar o mostrar elementos representados en un diccionario cambiando su propiedad de visibilidad.

    Parámetros:
        - diccionario (dict): Un diccionario que contiene elementos con propiedades de visibilidad.
        - visibilidad (bool): Un valor booleano que determina si los elementos deben ser visibles (True) u ocultos (False).

    Retorno:
        Esta función no retorna ningún valor directamente, pero modifica el diccionario proporcionado para cambiar la visibilidad de sus elementos.
    '''
    for key in diccionario:
        diccionario[key]["visibilidad"] = visibilidad
        
        
        


  
