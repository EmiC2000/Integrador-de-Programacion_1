import pygame as pg
import sys
import modules.forms.base_form as base_form
import modules.forms.form_stage as form_stage
import modules.stage as stage_juego
import modules.particip_juego as particip_juego
from modules.classes.label_custom import Label
from modules.classes.button_custom import Button
from modules.classes.button_image_sound import ButtonImageSound
import modules.variables as var

def create_form_wish(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form wish.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)

    form['jugador'] = dict_form_data.get('jugador')

    form['wish_type'] = ''

    form['lbl_titulo'] = Label(
        pos=(var.DIMENSION_PANTALLA[0] // 2, 100),
        text='Seccion Bonus', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=var.colores.get('blanco'),
        outline_color = var.colores.get('negro'), outline_thickness = 2
    )

    form['lbl_subtitulo'] = Label(
        pos=(var.DIMENSION_PANTALLA[0] // 2, 150),
        text='Selecciona el deseo o huye', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=var.colores.get('naranja'),
        outline_color = var.colores.get('negro'), outline_thickness = 2,
    )

    form['btn_wish'] = Button(
        x = var.DIMENSION_PANTALLA[0] // 2 - 200, y = 200,
        text='', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=40,
        color=var.colores.get('verde'),
        outline_color = var.colores.get('negro'), outline_thickness = 2,
        on_click=init_wish, on_click_param=form
    )

    form['btn_cancel'] = Button(
        x = var.DIMENSION_PANTALLA[0] // 2 + 200, y = 200,
        text='CANCEL', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=40,
        outline_color = var.colores.get('negro'), outline_thickness = 2,
        on_click=click_resume, on_click_param='form_stage'
    )

    form['widgets_list'] = [
        form.get('lbl_titulo'),
        form.get('lbl_subtitulo'),
        form.get('btn_wish'),
        form.get('btn_cancel')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def update_wish_type(dict_form_data: dict, wish_type: str):
    """funcion el cual lleva a cabo update wish type.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.
        wish_type (tipo): descripcion del parametro wish_type.

    """
    dict_form_data['wish_type'] = wish_type
    dict_form_data.get('widgets_list')[2].update_text(text=dict_form_data.get('wish_type'), color=pg.Color('red'))

def click_resume(form_name: str):
    """funcion el cual lleva a cabo click resume.

    Args:
        form_name (tipo): descripcion del parametro form_name.

    """
    base_form.cambiar_pantalla(form_name)

def init_wish(form_dict_data: dict):
    """funcion el cual lleva a cabo init wish.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    wish_type = form_dict_data.get('wish_type')
    jugador = form_dict_data.get('jugador')
    
    stage_form = var.dict_forms_status.get('form_stage')
    stage = stage_form.get('stage')

    if wish_type == 'HEAL':
        wish = 'heal'
    else:
        wish = 'shield'
    
    stage_juego.modificar_estado_bonus(stage, wish)

    if wish_type == 'SHIELD':
        stage['escudo_activo'] = True
        stage['rondas_escudo'] = 1
        print("SISTEMA: Escudo activado desde el Formulario de Deseos")
    else: 
        hp_inicial = particip_juego.get_hp_inicial_participante(jugador)
        hp_actual = particip_juego.get_hp_participante(jugador)
        hp_perdida = hp_inicial - hp_actual

        hp_bonus = int(hp_perdida * 0.75)
        nuevo_hp = hp_actual + hp_bonus

        print(f'Anterior HP: {hp_actual} | Actual HP: {nuevo_hp}')
        particip_juego.set_hp_participante(jugador, nuevo_hp)
    
    click_resume('form_stage')

def update(form_dict_data: dict):
    """funcion el cual lleva a cabo update.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    base_form.update(form_dict_data)

def draw(form_dict_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    base_form.draw(form_dict_data)
    base_form.draw_widgets(form_dict_data)