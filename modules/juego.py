import pygame as pg
import modules.variables as var
import sys
import modules.forms.form_controller as form_controller
import modules.particip_juego as participante
import modules.sonido as sonido

def pythonisa():

    pg.init()

    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla_juego = pg.display.set_mode(var.DIMENSION_PANTALLA)
    # pg.mouse.set_visible(False)
    image_icon = pg.image.load('assets/img/titulo.png')
    image_iconX = 100
    image_iconY = 60


    sonido.set_volume(var.VOLUMEN_INICIAL)
    corriendo = True
    reloj = pg.time.Clock()
    datos_juego = {
        "puntaje": 0,
        "cantidad_vidas": var.CANTIDAD_VIDAS,
        "player": participante.inicializar_participante(pantalla=pantalla_juego, nombre='PLAYER'),
        "music_config": {
            "music_volume": var.VOLUMEN_INICIAL,
            "music_on": True,
            'music_init': False
        }
    }


    form_control = form_controller.create_form_controller(pantalla_juego, datos_juego)

    while corriendo:
        
        eventos = pg.event.get()
        reloj.tick(var.FPS)

        for evento in eventos:
            if evento.type == pg.QUIT:
                corriendo = False

        form_controller.update(form_control, eventos)


        pg.display.flip()
    
    pg.quit()
    sys.exit()
