import modules.auxiliar as aux
import pygame as pg

def inicializar_carta(dict_card: dict, coords: list[int]) -> dict:
    """

    Args:
        dict_card (dict): diccionario de cartas.
        coords (list[int]): coordenadas de la posicion de las cartas.

    Returns:
        dict: devuelve un diccionario de los datos de las cartas. 
    """
    card = dict_card
    card['visible'] = False
    card['coordenadas'] = coords

    card['imagen'] = None
    card['rect'] = None

    return card

def esta_visible(dict_card: dict) -> bool:
    """funcion el cual lleva a cabo esta visible.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return dict_card.get('visible')

def cambiar_visibilidad(dict_card: dict):
    """funcion el cual lleva a cabo cambiar visibilidad.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.

    """
    dict_card['visible'] = not dict_card.get('visible')

def get_hp_carta(dict_card: dict) -> int:
    """funcion el cual lleva a cabo get hp carta.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return dict_card.get('hp')

def get_def_carta(dict_card: dict) -> int:
    """funcion el cual lleva a cabo get def carta.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return dict_card.get('def')

def get_atk_carta(dict_card: dict) -> int:
    """funcion el cual lleva a cabo get atk carta.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return dict_card.get('atk')

def asignar_coordenadas_carta(dict_card: dict, coordenadas: tuple[int]):
    """funcion el cual lleva a cabo asignar coordenadas carta.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.
        coordenadas (tipo): descripcion del parametro coordenadas.

    """
    dict_card['coordenadas'] = coordenadas

def draw_carta(dict_card: dict, screen: pg.Surface):
    """funcion el cual lleva a cabo draw carta.

    Args:
        dict_card (tipo): descripcion del parametro dict_card.
        screen (tipo): descripcion del parametro screen.

    """
    if dict_card.get('visible'):
        dict_card['imagen'] = aux.redimensionar_imagen(dict_card.get('ruta_frente'), 40)
    else:
        dict_card['imagen'] = aux.redimensionar_imagen(dict_card.get('ruta_reverso'), 40)
    
    dict_card['rect'] = dict_card.get('imagen').get_rect()
    dict_card['rect'].topleft = dict_card.get('coordenadas')

    screen.blit(dict_card.get('imagen'), dict_card.get('rect'))