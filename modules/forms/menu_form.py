import pygame as pg
import sys
import modules.forms.base_form as base_form
import modules.forms.form_stage as form_stage
from utn_fra.pygame_widgets import (ButtonSound)
from modules.classes.label_custom import Label
from modules.classes.button_custom import Button
from modules.classes.button_image_sound import ButtonImageSound
import modules.variables as var

def create_form_menu(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form menu.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)

    form['img_title'] = pg.image.load(var.IMG_TITULO) 
    form['img_title'] = pg.transform.scale(form['img_title'], (600, 100)) 
    form['title_pos'] = ( var.DIMENSION_PANTALLA[0] // 4, 30 )

    form['lbl_subtitulo'] = Label(
        pos = (var.DIMENSION_PANTALLA[0]// 2, 140),
        text= 'TRADING CARD GAME', 
        screen= form.get('screen'),
        font_path=var.FONT_HEINAN, font_size= 20, color=var.colores.get('blanco'),
        outline_color = var.colores.get('negro'), 
        outline_thickness = 2
    )

    form['btn_play'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=200,
        text='Play', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_PLAY,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=iniciar_stage, on_click_param='form_stage'
    )

    form['btn_tutorial'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=290,
        text='Tutorial', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_TUTORIAL,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=base_form.cambiar_pantalla, on_click_param='form_tutorial'
    )

    form['btn_ranking'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=380,
        text='Ranking', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_RANKING,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=base_form.cambiar_pantalla, on_click_param='form_ranking'
    )

    form['btn_options'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=470,
        text='Options', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_OPCIONES,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=base_form.cambiar_pantalla, on_click_param='form_options'
    )

    form['btn_exit'] = ButtonImageSound(
    x=var.DIMENSION_PANTALLA[0] // 2, y=560,
    text='Exit', screen=form.get('screen'),
    sound_path=var.SONIDO_CLICK,
    image_path=var.IMG_BTN_EXIT,
    dimension_scale = var.DIMENSION_BOTONES,        
    on_click=base_form.salir_juego, on_click_param=' '
    )

    form['widgets_list'] = [
        form.get('lbl_subtitulo'),
        form.get('btn_play'),
        form.get('btn_tutorial'),
        form.get('btn_ranking'),
        form.get('btn_options'),
        form.get('btn_exit')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def iniciar_stage(form_name: str):
    """funcion el cual lleva a cabo iniciar stage.

    Args:
        form_name (tipo): descripcion del parametro form_name.

    """
    base_form.cambiar_pantalla(form_name)
    stage_form = var.dict_forms_status.get(form_name)
    form_stage.iniciar_nueva_partida(stage_form)

def draw(dict_form_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    """
    base_form.draw(dict_form_data)
    screen = dict_form_data.get('screen')
    screen.blit(dict_form_data['img_title'], dict_form_data['title_pos'])
    base_form.draw_widgets(dict_form_data)

def update(dict_form_data: dict):
    """funcion el cual lleva a cabo update.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    """
    base_form.update(dict_form_data)
    if not dict_form_data.get('music_config').get('music_init'):
        base_form.music_on(dict_form_data)
        dict_form_data['music_config']['music_init'] = True
