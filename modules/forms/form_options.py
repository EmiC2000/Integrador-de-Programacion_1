import pygame as pg
import sys
import modules.forms.base_form as base_form
import modules.variables as var
import modules.sonido as sonido
from modules.classes.label_custom import Label
from modules.classes.button_custom import Button
from modules.classes.button_image_sound import ButtonImageSound
from modules.classes.slider import Slider as Sl

def create_form_options(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form options.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)

    form['lbl_titulo'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, 100),
        text='OPTIONS', screen=form.get('screen'),
        font_path=var.FONT_SAIYAN, font_size=45, color=var.colores.get('azul'),
        outline_color = var.colores.get('negro'), outline_thickness = 3,
    )

    form['btn_music_on'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=200,
        text='MUSIC ON', screen=form.get('screen'),
        color=var.colores.get('naranja'),
        font_path=var.FONT_HEINAN, font_size=40,
        outline_color = var.colores.get('negro'), outline_thickness = 3,
        on_click=activar_musica, on_click_param=form
    )
    
    form['btn_music_off'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=260,
        text='MUSIC OFF', screen=form.get('screen'),
        color=var.colores.get('naranja'),
        font_path=var.FONT_HEINAN, font_size=40,
        outline_color = var.colores.get('negro'), outline_thickness = 3,
        on_click=desactivar_musica, on_click_param=form
    )

    form['sli_vol'] = Sl( 
        pos=(var.DIMENSION_PANTALLA[0] // 2, var.SLIDER_Y_POS),
        size= var.DIMENSION_SLIDER,
        val_ini=sonido.get_actual_volume(), 
        min=0, 
        max=100,
        screen=form.get('screen'),
        progress_color= var.colores.get('azul'),
        handle_color= var.colores.get('naranja'),
        on_change=sonido.set_volume
    )
    
    form['lbl_vol'] = Label(
        pos = (var.DIMENSION_PANTALLA[0] // 2, var.SLIDER_Y_POS - 80 ), 
        text=f'{form["sli_vol"].get_value():.0f}',
        screen=form.get('screen'),
        font_path=var.FONT_HEINAN, font_size=45, color=var.colores.get('naranja'),
        outline_color = var.colores.get('negro'), outline_thickness = 3,
    )

    form['btn_volver'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2, y=500,
        text='Salir', screen=form.get('screen'),
        sound_path=var.SONIDO_CLICK,
        image_path=var.IMG_BTN_VOLVER,
        dimension_scale = var.DIMENSION_BOTONES,
        on_click=cambiar_pantalla, on_click_param='form_menu'
    )

    form['widgets_list'] = [
        form.get('lbl_titulo'),
        form.get('btn_music_on'),
        form.get('btn_music_off'),
        form.get('sli_vol'),
        form.get('lbl_vol'),
        form.get('btn_volver')
    ]

    var.dict_forms_status[form.get('name')] = form

    return form

def activar_musica(form_dict_data: dict):
    """funcion el cual lleva a cabo activar musica.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    form_dict_data['music_config']['music_on'] = True
    base_form.music_on(form_dict_data)

def desactivar_musica(form_dict_data: dict):
    """funcion el cual lleva a cabo desactivar musica.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    form_dict_data['music_config']['music_on'] = False
    print("Musica Activa: {form_dict_data['music_config']['music_on']}")
    sonido.stop_music()

def cambiar_pantalla(form_name: str):
    """funcion el cual lleva a cabo cambiar pantalla.

    Args:
        form_name (tipo): descripcion del parametro form_name.

    """
    base_form.set_active(form_name)

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
    
    slider_vol = form_dict_data.get('sli_vol')
    label_vol = form_dict_data.get('lbl_vol')
    
    if slider_vol and label_vol:
        nuevo_valor_volumen = slider_vol.get_value()
        
        sonido.set_volume(nuevo_valor_volumen) 
    
        texto_actualizado = f'{nuevo_valor_volumen:.0f}'
        
        color_label = var.colores.get('naranja')
        label_vol.outline_color = var.colores.get('negro')
        label_vol.outline_thickness = 3
    
        label_vol.update_text(texto_actualizado, color_label)