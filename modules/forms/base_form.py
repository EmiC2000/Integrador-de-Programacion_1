import pygame as pg
import modules.variables as var
import modules.sonido as sonido
import inspect


def create_base_form(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create base form.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = {}
    form['name'] = dict_form_data.get('name')
    form['screen'] = dict_form_data.get('screen')
    form['active'] = dict_form_data.get('active')
    form['x_coord'] = dict_form_data.get('coord')[0]
    form['y_coord'] = dict_form_data.get('coord')[1]

    form['music_path'] = dict_form_data.get('music_path')
    form['surface'] = pg.image.load(dict_form_data.get('background')).convert_alpha()
    form['surface'] = pg.transform.scale(form.get('surface'), dict_form_data.get('screen_dimentions'))

    form['rect'] = form.get('surface').get_rect()
    form['rect'].x = dict_form_data.get('coord')[0]
    form['rect'].y = dict_form_data.get('coord')[1]
    form['music_config'] = dict_form_data.get('music_config')
    return form

def draw_widgets(form_data: dict):
    """funcion el cual lleva a cabo draw widgets.

    Args:
        form_data (tipo): descripcion del parametro form_data.

    """
    for widget in form_data.get('widgets_list'):
        widget.draw()

def update_widgets(form_data: dict, event_list: list = None):

    """funcion el cual lleva a cabo update widgets.

    Args:
        form_data (tipo): descripcion del parametro form_data.
        event_list (list): lista de eventos de pygame para widgets que los requieren.

    """
    for widget in form_data.get('widgets_list'):
        
        if event_list is not None:
            try:
                sig = inspect.signature(widget.update)
                params = len(sig.parameters)
            except (ValueError, TypeError):
                params = 0

            if params >= 1:
                widget.update(event_list)
                continue

        widget.update()

def set_active(form_name: str, change_music: bool = True):
    """funcion el cual lleva a cabo set active.

    Args:
        form_name (tipo): descripcion del parametro form_name.
        change_music (tipo): descripcion del parametro change_music.

    """
    for form in var.dict_forms_status.values():
        form['active'] = False
    form_activo = var.dict_forms_status[form_name]
    form_activo['active'] = True

    print(f"DEBUG: set_active -> activado {form_name}, change_music={change_music}")

    pg.event.clear([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP])
    print('DEBUG: Eventos de mouse limpiados al cambiar de pantalla')

    if change_music:
        music_off(form_activo)
        music_on(form_activo)

def music_on(form_dict_data: dict):
    """funcion el cual lleva a cabo music on.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    print(f"Musica activa: {form_dict_data.get('music_config').get('music_on')}")
    if form_dict_data.get('music_config').get('music_on'):
        ruta_musica = form_dict_data.get('music_path')
        print(f'Ruta musica: {ruta_musica}')
        sonido.set_music_path(ruta_musica)
        sonido.play_music()

def music_off(form_dict_data: dict):
    """funcion el cual lleva a cabo music off.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    if form_dict_data.get('music_config').get('music_on'):
        sonido.stop_music()

def cambiar_pantalla(form_name: str, change_music: bool = True):
    """funcion el cual lleva a cabo cambiar pantalla.

    Args:
        form_name (tipo): descripcion del parametro form_name.
        change_music (tipo): descripcion del parametro change_music.

    """
    set_active(form_name, change_music)

import pygame as pg
import sys 
import modules.variables as var
import modules.sonido as sonido


def salir_juego(_):
    """funcion el cual lleva a cabo salir juego.

    Args:
        _ (tipo): descripcion del parametro _.

    """
    print('Saliendo del juego desde el boton')
    pg.quit()
    sys.exit()

def events_handler(dict_form_data: dict):
    """
    Maneja todos los eventos de Pygame para el formulario activo.
    Incluye la lógica de colisión (handle_click) para los botones y devuelve la
    lista completa de eventos para que widgets que la necesitan (p.ej. TextBox)
    puedan procesarlos en su `update(event_list)`.
    """
    events = pg.event.get()

    for event in events:
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            for widget in dict_form_data.get('widgets_list'):
                
                if hasattr(widget, 'handle_click') and widget.rect.collidepoint(x, y):
                    
                    widget.handle_click() 
                    break 
                        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        for widget in dict_form_data.get('widgets_list'):
            
            if hasattr(widget, 'handle_input'):
                widget.handle_input(event)
        
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            for widget in dict_form_data.get('widgets_list'):
                if hasattr(widget, 'handle_click') and widget.rect.collidepoint(x, y):
                    if not (hasattr(widget, 'dragging') and widget.dragging):
                        widget.handle_click() 
                        break

    return events

def update(form_data: dict):
    """funcion el cual lleva a cabo update.

    Args:
        form_data (tipo): descripcion del parametro form_data.

    """
    events = events_handler(form_data)
    update_widgets(form_data, events)

def draw(form_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        form_data (tipo): descripcion del parametro form_data.

    """
    form_data['screen'].blit(form_data.get('surface'), form_data.get('rect'))