import pygame as pg

########## Configs Juego ##########
DIMENSION_PANTALLA = (1080, 600)
TITULO_JUEGO = 'Dragon Ball Z Trading Card Game'
FPS = 60
dict_forms_status = {}
STAGE_TIMER = 400
JSON_CONFIGS = 'configs.json'
JSON_INFO_CARDS = 'info_cartas.json'
DIMENSION_BOTONES = (300, 70)
SLIDER_Y_POS = 400
DIMENSION_SLIDER = (300, 100)
########## Configs Player ##########
CANTIDAD_VIDAS = 30000

########## Configs Audio ##########
VOLUMEN_INICIAL = 51

########## Fuentes ##########
FONT_SAIYAN = 'assets/fonts/saiyan.ttf'
FONT_HEINAN = 'assets/fonts/heinan.ttf'

########## Fondos de formularios ##########
FONDO_MENU = 'assets/img/background/menu.jpg'
FONDO_RANKING = 'assets/img/background/ranking.jpg'
FONDO_OPTIONS = 'assets/img/background/opciones.png'
FONDO_PAUSE = 'assets/img/background/pausa.jpg'
FONDO_STAGE = 'assets/img/background/fondo_5.png'
FONDO_NAME = 'assets/img/background/fondo_7.png'
FONDO_WISH = 'assets/img/background/form_wish.jpg'
FONDO_VICTORIA = 'assets/img/background/victoria.jpg'
FONDO_DERROTA = 'assets/img/background/derrota.jpg'

########## IMAGENES BOTONES ##########
IMG_BTN_PLAY = 'assets/img/buttons/jugar.png'
IMG_BTN_TUTORIAL = 'assets/img/buttons/tutorial.png'
IMG_BTN_RANKING = 'assets/img/buttons/ranking.png'
IMG_BTN_OPCIONES = 'assets/img/buttons/opciones.png'
IMG_BTN_EXIT = 'assets/img/buttons/salir.png'
IMG_BTN_VOLVER = 'assets/img/buttons/volver.png'
IMG_ICON_HEAL = 'assets/img/icon_heal.png'
IMG_BTN_RIGHT = 'assets/img/buttons/derecha.png'
IMG_BTN_LEFT = 'assets/img/buttons/izquierda.png'

########## IMAGENES ##########
IMG_TITULO = 'assets/img/titulo.png'
IMG_TUTORIAL_1 = 'assets/img/frieza_25.png'
IMG_TUTORIAL_2 = 'assets/img/frieza_50.png'
IMG_TUTORIAL_3 = 'assets/img/frieza_75.png'


########## Archivos ##########
RANKING_CSV = 'puntajes.csv'

########## Colores ##########
colores = {
    "amarillo": pg.Color('yellow'),
    "azul": pg.Color('blue'),
    "blanco": pg.Color('white'),
    "cian": pg.Color('cyan'),
    "naranja": pg.Color('orange'),
    "negro": pg.Color('black'),
    "rojo": pg.Color('red'),
    "rosa": pg.Color('pink'),
    "verde": pg.Color('green')
}
########## Mouse Pointer ##########
MOUSE_POINTER = 'assets/img/cursor/cursordbz.png'
DIMENSION_CURSOR = (20,10)

########## RUTAS MUSICA ##########
MUSICA_RANKING = 'assets/sound/ranking.mp3'
MUSICA_MENU = 'assets/sound/music.mp3'
MUSICA_OPTIONS = 'assets/sound/music.mp3'
MUSICA_PAUSE = 'assets/sound/level_1.mp3'
MUSICA_STAGE = 'assets/sound/stage.mp3'

########## RUTAS SONIDO ##########
SONIDO_CLICK = 'assets/sound/click_scouter.ogg'