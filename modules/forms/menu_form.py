import pygame as pg
import sys
import modules.forms.base_form as base_form
import modules.forms.form_stage as form_stage
from utn_fra.pygame_widgets import (
    Label, Button, ButtonSound,ButtonImageSound
)
import modules.variables as var

def create_form_menu(dict_form_data: dict) -> dict:
    form = base_form.create_base_form(dict_form_data)

    form['img_title'] = pg.image.load(var.IMG_TITULO) 
    form['img_title'] = pg.transform.scale(form['img_title'], (600, 100)) 
    form['title_pos'] = ( var.DIMENSION_PANTALLA[0] // 2 - form['img_title'].get_width() // 2, 30 )

    form['lbl_subtitulo'] = Label(
        var.DIMENSION_PANTALLA[0] // 2, y = 140,
        text= 'TRADING CARD GAME', screen= form.get('screen'),
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

    form['btn_ranking'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=300,
        text='Ranking', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_RANKING,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=base_form.cambiar_pantalla, on_click_param='form_ranking'
    )

    form['btn_options'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=400,
        text='Options', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_OPCIONES,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=base_form.cambiar_pantalla, on_click_param='form_options'
    )

    form['btn_exit'] = ButtonImageSound(
    x=var.DIMENSION_PANTALLA[0] // 2, y=500,
    text='Exit', screen=form.get('screen'),
    sound_path=var.SONIDO_CLICK,
    image_path=var.IMG_BTN_EXIT,
    dimension_scale = var.DIMENSION_BOTONES,        
    on_click=base_form.salir_juego, on_click_param=' '
    )

    form['widgets_list'] = [
        form.get('lbl_subtitulo'),
        form.get('btn_play'),
        form.get('btn_ranking'),
        form.get('btn_options'),
        form.get('btn_exit')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def iniciar_stage(form_name: str):
    base_form.cambiar_pantalla(form_name)
    stage_form = var.dict_forms_status.get(form_name)
    form_stage.iniciar_nueva_partida(stage_form)

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)
    screen = dict_form_data.get('screen')
    screen.blit(dict_form_data['img_title'], dict_form_data['title_pos'])
    base_form.draw_widgets(dict_form_data)

def update(dict_form_data: dict):
    base_form.update(dict_form_data)
    if not dict_form_data.get('music_config').get('music_init'):
        base_form.music_on(dict_form_data)
        dict_form_data['music_config']['music_init'] = True
