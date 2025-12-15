import pygame as pg
import sys
import modules.forms.base_form as base_form
import modules.forms.form_stage as form_stage
from modules.label_custom import Label
from modules.button_custom import Button
import modules.variables as var
import modules.sonido as sonido

def create_form_pause(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form pause.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)
    form['last_volume'] = None
    
    form['lbl_titulo'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 100),
        text='PAUSE', screen=form.get('screen'),
        font_path=var.FONT_SAIYAN, font_size=100, color=var.colores.get('naranja'),
        outline_color=(var.colores.get('negro')), outline_thickness=3
    )

    form['btn_resume'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=200,
        text='RESUME', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=70,
        color=var.colores.get('blanco'),
        outline_color=(var.colores.get('negro')), outline_thickness=3,
        on_click=cambiar_pantalla, on_click_param={'form': form, 'form_name': 'form_stage'}
    )

    form['btn_restart'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=300,
        text='RESTART STAGE', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=70,
        color=var.colores.get('blanco'),
        outline_color=(var.colores.get('negro')), outline_thickness=3,
        on_click=restart_stage, on_click_param={'form': form, 'form_name': 'form_stage'}
    )

    form['btn_back'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=400,
        text='BACK TO MENU', screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=70,
        color=var.colores.get('blanco'),
        outline_color=(var.colores.get('negro')), outline_thickness=3,
        on_click=base_form.cambiar_pantalla, on_click_param='form_menu'
    )

    form['widgets_list'] = [
        form.get('lbl_titulo'),
        form.get('btn_resume'),
        form.get('btn_restart'),
        form.get('btn_back')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def cambiar_pantalla(params: dict):
    """funcion el cual lleva a cabo cambiar pantalla.

    Args:
        params (tipo): descripcion del parametro params.

    """
    last_vol = params.get('form').get('last_volume')
    base_form.cambiar_pantalla(params.get('form_name'), change_music=False)
    set_last_vol(last_vol)

def restart_stage(params: dict):
    """funcion el cual lleva a cabo restart stage.

    Args:
        params (tipo): descripcion del parametro params.

    """
    stage_form = var.dict_forms_status.get(params.get('form_name'))
    # base_form.cambiar_pantalla(params.get('form_name'))
    cambiar_pantalla(params)
    form_stage.iniciar_nueva_partida(stage_form)


def set_last_vol(vol: int):
    """funcion el cual lleva a cabo set last vol.

    Args:
        vol (tipo): descripcion del parametro vol.

    """
    sonido.set_volume(vol)

def save_last_vol(form_dict_data: dict):
    """funcion el cual lleva a cabo save last vol.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    form_dict_data['last_volume'] = sonido.get_actual_volume()
    set_last_vol(10)

def draw(form_dict_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    base_form.draw(form_dict_data)
    base_form.draw_widgets(form_dict_data)

def update(form_dict_data: dict):
    """funcion el cual lleva a cabo update.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    base_form.update(form_dict_data)