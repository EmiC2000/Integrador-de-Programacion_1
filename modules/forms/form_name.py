import pygame as pg
import modules.forms.base_form as base_form
import modules.forms.form_stage as form_stage
import modules.particip_juego as particip_juego
import modules.auxiliar as aux

from utn_fra.pygame_widgets import (TextBox)
from modules.classes.label_custom import Label
from modules.classes.button_custom import Button
from modules.classes.button_image_sound import ButtonImageSound

import modules.variables as var

def create_form_name(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form name.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)
    form['jugador'] = dict_form_data.get('jugador')
    form['info_submitida'] = False

    form['lbl_titulo'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 100),
        text='Victoria!', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=pg.Color('white'),
        outline_color= var.colores.get('negro'),
        outline_thickness=2
    )

    form['lbl_subtitulo'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 150),
        text='Escriba su nombre', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=pg.Color('white'),
        outline_color= var.colores.get('negro'),
        outline_thickness=2
    )

    form['lbl_score'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 210),
        text=f'{particip_juego.get_score_participante(form.get('jugador'))}', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=pg.Color('white'),
        outline_color= var.colores.get('negro'),
        outline_thickness=2
    )

    form['lbl_nombre_texto'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 270),
        text='', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=pg.Color('white'),
        outline_color= var.colores.get('negro'),
        outline_thickness=2
    )

    form['text_box'] = TextBox(
        x=var.DIMENSION_PANTALLA[0] // 2, y=280,
        text=f'_________________', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=25, color=pg.Color('white')
    )

    form['btn_submit'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=370,
        text='CONFIRMAR NOMBRE', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=40,
        on_click=submit_name, on_click_param=form
    )

    form['widgets_list'] = [
        form.get('lbl_titulo'),
        form.get('lbl_subtitulo'),
        form.get('lbl_score'),
        form.get('lbl_nombre_texto'),
        form.get('text_box'),
        form.get('btn_submit')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def update_texto_victoria(form_dict_data: dict, win_status: bool):
    """funcion el cual lleva a cabo update texto victoria.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.
        win_status (tipo): descripcion del parametro win_status.

    """
    if win_status:
        mensaje = 'Victoria!'
        nueva_img = pg.image.load(var.FONDO_VICTORIA).convert_alpha()
    else:
        mensaje = 'Derrota!'
        nueva_img = pg.image.load(var.FONDO_DERROTA).convert_alpha()

    nueva_img = pg.transform.scale(nueva_img, var.DIMENSION_PANTALLA)
    # `base_form` dibuja usando la key 'surface', así que actualizamos esa Surface directamente
    form_dict_data['surface'] = nueva_img
    print(f"DEBUG: update_texto_victoria -> mensaje={mensaje}")
    if form_dict_data.get('widgets_list'):
        form_dict_data.get('widgets_list')[0].update_text(text=mensaje, color=pg.Color('white'))
    else:
        print('WARN: form_name widgets_list vacío, no puedo actualizar etiqueta')

def clear_text(form_data: dict):
    """funcion el cual lleva a cabo clear text.

    Args:
        form_data (tipo): descripcion del parametro form_data.

    """
    form_data['text_box'].writing = ''

def submit_name(form_data: dict):

    """funcion el cual lleva a cabo submit name.

    Args:
        form_data (tipo): descripcion del parametro form_data.

    """
    nombre_jugador = form_data.get('lbl_nombre_texto').text
    particip_juego.set_nombre_participante(form_data.get('jugador'), nombre_jugador)
    
    nombre_jugador_seteado = particip_juego.get_nombre_participante(form_data.get('jugador'))
    puntaje_jugador = particip_juego.get_score_participante(form_data.get('jugador'))
    
    print(f'NOMBRE JUGADOR: {nombre_jugador_seteado} - {puntaje_jugador}')
    data_to_csv = particip_juego.info_to_csv(form_data.get('jugador'))
    aux.guardar_info_csv(data_to_csv)

    form_data['info_submitida'] = True

    base_form.set_active('form_ranking')

def update(form_dict_data: dict, event_list: list[pg.event.Event]):
    """funcion el cual lleva a cabo update.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.
        event_list (tipo): descripcion del parametro event_list.

    """
    form_dict_data['score'] = particip_juego.get_score_participante(form_dict_data.get('jugador'))

    form_dict_data.get('widgets_list')[2].update_text(text=f'SCORE: {form_dict_data.get("score")}', color=pg.Color('cyan'))
    form_dict_data.get('widgets_list')[3].update_text(text=f'{form_dict_data.get('text_box').writing.upper()[:form_dict_data.get('limit_char')]}', color=pg.Color('cyan'))

    form_dict_data.get('text_box').writing = form_dict_data.get('text_box').writing[:form_dict_data.get('limit_char')]
    form_dict_data.get('text_box').update(event_list)
    base_form.update(form_dict_data)

def draw(form_dict_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    base_form.draw(form_dict_data)
    base_form.draw_widgets(form_dict_data)
    form_dict_data.get('text_box').draw()