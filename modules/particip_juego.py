import pygame as pg
import modules.carta as carta
import modules.variables as var
import modules.auxiliar as aux
from functools import reduce

def inicializar_participante(pantalla: pg.Surface, nombre: str = 'PC'):
    """funcion el cual lleva a cabo inicializar participante.

    Args:
        pantalla (tipo): descripcion del parametro pantalla.
        nombre (tipo): descripcion del parametro nombre.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    player = {}
    player['nombre'] = nombre
    player['hp_inicial'] = 1
    player['hp_actual'] = 1
    player['attack'] = 1
    player['defense'] = 1
    player['score'] = 0

    player['mazo_asignado'] = []
    player['cartas_mazo'] = []
    player['cartas_mazo_usadas'] = []

    player['screen'] = pantalla
    player['pos_deck_inicial'] = (0,0)
    player['pos_deck_jugado'] = (0,0)

    return player

def get_hp_participante(participante: dict) -> int:
    """funcion el cual lleva a cabo get hp participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('hp_actual')

def get_hp_inicial_participante(participante: dict) -> int:
    """funcion el cual lleva a cabo get hp inicial participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('hp_inicial')

def get_attack_participante(participante: dict) -> int:
    """funcion el cual lleva a cabo get attack participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('attack')

def get_defense_participante(participante: dict) -> int:
    """funcion el cual lleva a cabo get defense participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('defense')

def get_nombre_participante(participante: dict) -> str:
    """funcion el cual lleva a cabo get nombre participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('nombre')

def get_cartas_iniciales_participante(participante: dict) -> list[dict]:
    """funcion el cual lleva a cabo get cartas iniciales participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('mazo_asignado')

def get_cartas_restantes_participante(participante: dict) -> list[dict]:
    """funcion el cual lleva a cabo get cartas restantes participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('cartas_mazo')

def get_cartas_jugadas_participante(participante: dict) -> list[dict]:
    """funcion el cual lleva a cabo get cartas jugadas participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('cartas_mazo_usadas')

def get_coordenadas_mazo_inicial(participante: dict):
    """funcion el cual lleva a cabo get coordenadas mazo inicial.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('pos_deck_inicial')

def get_coordenadas_mazo_jugada(participante: dict):
    """funcion el cual lleva a cabo get coordenadas mazo jugada.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('pos_deck_jugado')

def get_carta_actual_participante(participante: dict):
    """funcion el cual lleva a cabo get carta actual participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('cartas_mazo_usadas')[-1]

def setear_stat_participante(participante: dict, stat: str, valor: int):
    """funcion el cual lleva a cabo setear stat participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        stat (tipo): descripcion del parametro stat.
        valor (tipo): descripcion del parametro valor.

    """
    participante[stat] = valor

def set_cartas_participante(participante: dict, lista_cartas: list[dict]):

    """funcion el cual lleva a cabo set cartas participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        lista_cartas (tipo): descripcion del parametro lista_cartas.

    """
    for carta_b in lista_cartas:
        coordenada = get_coordenadas_mazo_inicial(participante)
        carta_b['coordenadas'] = coordenada
    
    participante['mazo_asignado'] = lista_cartas
    participante['cartas_mazo'] = lista_cartas.copy()

def set_score_participante(participante: dict, score: int):
    """funcion el cual lleva a cabo set score participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        score (tipo): descripcion del parametro score.

    """
    participante['score'] = score

def get_score_participante(participante: dict) -> int:
    """funcion el cual lleva a cabo get score participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return participante.get('score')

def set_nombre_participante(participante: dict, nuevo_nombre: str):
    """funcion el cual lleva a cabo set nombre participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        nuevo_nombre (tipo): descripcion del parametro nuevo_nombre.

    """
    participante['nombre'] = nuevo_nombre

def set_hp_participante(participante: dict, hp_actual: int):
    """funcion el cual lleva a cabo set hp participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        hp_actual (tipo): descripcion del parametro hp_actual.

    """
    participante['hp_actual'] = hp_actual

def add_score_participante(participante: dict, score: int):
    """funcion el cual lleva a cabo add score participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        score (tipo): descripcion del parametro score.

    """
    participante['score'] += score

def asignar_stats_iniciales_participante(participante: dict):
    """funcion el cual lleva a cabo asignar stats iniciales participante.

    Args:
        participante (tipo): descripcion del parametro participante.

    """
    participante['hp_inicial'] = aux.reducir(
        carta.get_hp_carta,
        participante.get('mazo_asignado')
    )

    participante['hp_actual'] = participante['hp_inicial']

    participante['attack'] = aux.reducir(
        carta.get_atk_carta,
        participante.get('mazo_asignado')
    )

    participante['defense'] = aux.reducir(
        carta.get_def_carta,
        participante.get('mazo_asignado')
    )

def chequear_valor_negativo(stat: int):
    """funcion el cual lleva a cabo chequear valor negativo.

    Args:
        stat (tipo): descripcion del parametro stat.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    if stat < 0:
        return 0
    return stat

def restar_stats_participante(participante: dict, carta_g: dict, is_critic: bool):

    """
    Comparar ataque carta con la defensa de la carta del jugador,
    la resta es la que vamos a restarle al jugador
    """
    damage_mul = 1
    if is_critic:
        damage_mul = 3

    carta_jugador = participante.get('cartas_mazo_usadas')[-1]
    damage = carta.get_atk_carta(carta_g) - carta.get_def_carta(carta_jugador)
    damage *= damage_mul

    participante['hp_actual'] = chequear_valor_negativo(participante.get('hp_actual') - damage)
    participante['attack'] -= carta.get_atk_carta(carta_jugador)
    participante['defense'] -= carta.get_def_carta(carta_jugador)

def jugar_carta(participante: dict):
    """funcion el cual lleva a cabo jugar carta.

    Args:
        participante (tipo): descripcion del parametro participante.

    """
    if participante.get('cartas_mazo'):
        print(f'El jugador {participante.get("nombre")} tiene {len(participante.get('cartas_mazo'))} cartas')
        carta_actual = participante.get('cartas_mazo').pop()
        carta.cambiar_visibilidad(carta_actual)
        carta.asignar_coordenadas_carta(carta_actual, get_coordenadas_mazo_jugada(participante))
        participante.get('cartas_mazo_usadas').append(carta_actual)
    else:
        print(f'El jugador {participante.get("nombre")} no tiene cartas')
        

def info_to_csv(participante: dict):
    """funcion el cual lleva a cabo info to csv.

    Args:
        participante (tipo): descripcion del parametro participante.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    return f'{get_nombre_participante(participante)},{participante.get('score')}\n'

def reiniciar_datos_participante(player: dict):
    """funcion el cual lleva a cabo reiniciar datos participante.

    Args:
        player (tipo): descripcion del parametro player.

    """
    set_nombre_participante(player, 'PLAYER')
    set_score_participante(player, 0)
    set_cartas_participante(player, list())
    player['cartas_mazo_usadas'].clear()
    setear_stat_participante(player, 'hp_inicial', 0)
    setear_stat_participante(player, 'hp_actual', 0)
    setear_stat_participante(player, 'ataque', 0)
    setear_stat_participante(player, 'defensa', 0)

def draw_participante(participante: dict, screen: pg.Surface):

    # Solo dibujamos la ultima de cada mazo
    # El mazo que aun no se dio vuelta y el mazo de cartas jugadas
    """funcion el cual lleva a cabo draw participante.

    Args:
        participante (tipo): descripcion del parametro participante.
        screen (tipo): descripcion del parametro screen.

    """
    if participante.get('cartas_mazo'):
        # print(f'Se dibuja carta restante de {participante.get("nombre")}')
        carta.draw_carta(participante.get('cartas_mazo')[-1], screen)
    
    if participante.get('cartas_mazo_usadas'):
        # print(f'Se dibuja carta usada de {participante.get("nombre")}')
        carta.draw_carta(participante.get('cartas_mazo_usadas')[-1], screen)

