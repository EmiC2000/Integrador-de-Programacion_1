import modules.variables as var
import json
import os
import pygame as pg
import random as rd



def mapear_valores(matriz: list[list], columna_a_mapear: int, callback):
    """funcion el cual lleva a cabo mapear valores.

    Args:
        matriz (list[list]): genera una matriz.
        columna_a_mapear (int): se .
        callback: descripcion del parametro callback.

    """
    for indice_fila in range(len(matriz)):
        # Saltar filas que no tengan la columna solicitada (robustez frente a CSV malformados)
        if len(matriz[indice_fila]) <= columna_a_mapear:
            continue
        valor = matriz[indice_fila][columna_a_mapear]
        matriz[indice_fila][columna_a_mapear] = callback(valor)

def parsear_entero(valor: str):
    """pasar de un valor string a entero

    Args:
        valor (str): parametro valor dado en string

    Returns:
        valor(int):
        valor dado en string anteriormente convertido a entero
    """
    if valor.isdigit():
        return int(valor)
    return valor

def crear_matriz_datos(texto: str) -> list[list]:
    """Creacion de matriz de datos.

    Args:
        texto (str): datos dados en str.

    Returns:
        ranking: devuelve una matriz con los datos cargados.
    """
    ranking = []
    for linea in texto.split('\n'):
        if linea:
            lista_datos_linea = linea.split(',')
            ranking.append(lista_datos_linea)
    return ranking

def cargar_ranking(file_path: str, top: int = 10):
    """funcion el cual lleva a cabo la carga del ranking.

    Args:
        file_path (str): direccion del archivo en formato string.
        top (int): datos cargados con limite de 10.

    Returns:
        ranking[:top]: devuelve la matriz ranking segmentado a 10 elementos.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        texto = file.read()
        ranking = crear_matriz_datos(texto)

    mapear_valores(ranking, columna_a_mapear=1, callback=parsear_entero)

    ranking = ranking[1:]
    ranking = [fila for fila in ranking if len(fila) > 1 and isinstance(fila[1], int)]
    ranking.sort(key=lambda fila: fila[1], reverse=True)
    return ranking[:top]

def cargar_configs(file_path: str) -> dict:
    """Carga de la configuracion del juego mediante la carga del archivo JSON.

    Args:
        file_path (str): direcctorio donde se encuentra el archivo.

    Returns:
        data: retorna un diccionario con los datos cargados desde el direcctorio 
        donde se encuentra el archivo JSON.
    """
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def cargar_configs_stage(stage_data: dict):
    """funcion el cual lleva a cabo cargar configs stage.

    Args:
        stage_data (tipo): descripcion del parametro stage_data.

    """
    if not stage_data.get('juego_finalizado') and not stage_data.get('data_cargada'):
        configs_globales = cargar_configs(var.JSON_CONFIGS)
        stage_data['configs'] = configs_globales.get('nivel_1')
        stage_data['ruta_mazos'] = stage_data.get('configs').get('ruta_mazos')
        stage_data['nombre_mazo_enemigo'] = stage_data.get('configs').get('mazo_enemigo')
        stage_data['nombre_mazo_jugador'] = stage_data.get('configs').get('mazo_player')
        stage_data['ruta_mazo_jugador'] = stage_data.get('configs').get('ruta_mazo_player')
        stage_data['coords_inicial_mazo_enemigo'] = stage_data.get('configs').get('coordenada_mazo_enemigo')
        stage_data['coords_inicial_mazo_player'] = stage_data.get('configs').get('coordenada_mazo_player')
        stage_data['cantidad_cartas_jugadores'] = stage_data.get('configs').get('cantidad_cartas_jugadores')

def guardar_info_csv(informacion: str):
    """funcion el cual lleva a cabo guardar info csv.

    Args:
        informacion (tipo): descripcion del parametro informacion.

    """
    with open(var.RANKING_CSV, 'a', encoding='utf-8') as file:
        file.write(informacion)
        print(f'INFORMACION GUARDADA -> {informacion}')

def generar_bd_cartas(path_mazo: str) -> dict:
    """funcion el cual lleva a cabo generar bd cartas.

    Args:
        path_mazo (tipo): descripcion del parametro path_mazo.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    cartas_dict = {
        "cartas": {}
    }

    for root, dir, files in os.walk(path_mazo):
        reverse_path = ''
        deck_cards = []
        deck_name = ''
        for carta in files:
            card_path = os.path.join(root, carta)
            deck_name = root.replace('\\', '/').split('/')[-1]
            print(f'DECK NAME: {deck_name}')

            if 'reverse' in card_path:
                reverse_path = card_path.replace('\\', '/')
            else:
                card_path = card_path.replace('\\', '/')
                filename = carta
                filename = filename.replace('.png', '')
                datos_crudo = filename.split('_')

                datos_card = {
                    'id': datos_crudo[0],
                    'atk': int(datos_crudo[4]),
                    'def': int(datos_crudo[6]),
                    'hp': int(datos_crudo[2]),
                    'bonus': int(datos_crudo[-1]),
                    'ruta_frente': card_path,
                    'ruta_reverso': ''
                }
                deck_cards.append(datos_card)
        
        for index_carta in range(len(deck_cards)):
            deck_cards[index_carta]['ruta_reverso'] = reverse_path
        
        if deck_name:
            cartas_dict['cartas'][deck_name] = deck_cards
    return cartas_dict

def guardar_info_cartas(ruta_archivo: str, dict_cards: dict):
    """funcion el cual lleva a cabo guardar info cartas.

    Args:
        ruta_archivo (tipo): descripcion del parametro ruta_archivo.
        dict_cards (tipo): descripcion del parametro dict_cards.

    """
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(dict_cards, file, indent=4)

def cargar_bd_cartas(stage_data: dict):
    """funcion el cual lleva a cabo cargar bd cartas.

    Args:
        stage_data (tipo): descripcion del parametro stage_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    if not stage_data.get('juego_finalizado'):
        if os.path.exists(var.JSON_INFO_CARDS) and os.path.isfile(var.JSON_INFO_CARDS):
            print('================================== CARGANDO BD CARTAS DESDE FILE ==================================')
            cartas = cargar_configs(var.JSON_INFO_CARDS)
            
        else:
            print('================================== CARGANDO BD CARTAS DESDE DIR ==================================')
            cartas = generar_bd_cartas(stage_data.get('ruta_mazos'))
            guardar_info_cartas(var.JSON_INFO_CARDS, cartas)
            
        db_cartas = cartas.get('cartas', {})
        if not db_cartas:
            print("❌ ERROR CRÍTICO: No se encontraron mazos en la base de datos.")
            return

        mazos_disponibles = list(db_cartas.keys())
        
        if len(mazos_disponibles) > 1 and stage_data.get('mezclar_expansiones', True):
            print('🃏 Asignando mazos mezclados aleatoriamente (mezclar_expansiones=True)')
            pool = []
            for mazo_nombre, cartas_mazo in db_cartas.items():
                for carta in cartas_mazo:
                    c = carta.copy()
                    c['mazo_origen'] = mazo_nombre
                    pool.append(c)

            tam = int(stage_data.get('tam_mazo', 30))

            if len(pool) >= tam * 2:
                rd.shuffle(pool)
                stage_data['cartas_mazo_inicial_p'] = pool[:tam]
                stage_data['cartas_mazo_inicial_e'] = pool[tam: tam * 2]
            else:
                
                rd.shuffle(pool)

                if not pool:
                    stage_data['cartas_mazo_inicial_p'] = []
                    stage_data['cartas_mazo_inicial_e'] = []
                else:
                    stage_data['cartas_mazo_inicial_p'] = rd.choices(pool, k=tam)
                    stage_data['cartas_mazo_inicial_e'] = rd.choices(pool, k=tam)
        else:
            mazo_e_nombre = stage_data.get('nombre_mazo_enemigo') or mazos_disponibles[0]
            mazo_p_nombre = stage_data.get('nombre_mazo_jugador') or (mazos_disponibles[1] if len(mazos_disponibles) > 1 else mazos_disponibles[0])

            print(f"🃏 Asignando mazo Player: {mazo_p_nombre}")
            print(f"🃏 Asignando mazo Enemigo: {mazo_e_nombre}")

            stage_data['cartas_mazo_inicial_e'] = db_cartas.get(mazo_e_nombre, [])
            stage_data['cartas_mazo_inicial_p'] = db_cartas.get(mazo_p_nombre, [])


        print(f"✅ Cartas cargadas - Player: {len(stage_data['cartas_mazo_inicial_p'])} | Enemigo: {len(stage_data['cartas_mazo_inicial_e'])}")

def redimensionar_imagen(ruta_img: str, porcentaje_a_ajustar: int):
    """funcion el cual lleva a cabo redimensionar imagen.

    Args:
        ruta_img (tipo): descripcion del parametro ruta_img.
        porcentaje_a_ajustar (tipo): descripcion del parametro porcentaje_a_ajustar.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    imagen_raw = pg.image.load(ruta_img)
    ancho = imagen_raw.get_width()
    alto = imagen_raw.get_height()

    nuevo_alto = int( alto * float(f'0.{porcentaje_a_ajustar}'))
    nuevo_ancho = int( ancho * float(f'0.{porcentaje_a_ajustar}'))

    imagen_final = pg.transform.scale(imagen_raw, (nuevo_ancho, nuevo_alto))
    return imagen_final

def reducir(callback, iterable: list):
    """funcion el cual lleva a cabo reducir.

    Args:
        callback (tipo): descripcion del parametro callback.
        iterable (tipo): descripcion del parametro iterable.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    suma = 0
    for elemento in iterable:
        suma += callback(elemento)
    return suma

