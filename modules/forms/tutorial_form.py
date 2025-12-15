import pygame as pg
import modules.forms.base_form as base_form
from utn_fra.pygame_widgets import ButtonImage
import modules.variables as var
from modules.label_custom import Label
from modules.button_custom import Button

def create_form_tutorial(dict_form_data: dict) -> dict:
    """funcion el cual lleva a cabo create form tutorial.

    Args:
        dict_form_data (tipo): descripcion del parametro dict_form_data.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    form = base_form.create_base_form(dict_form_data)

    # --- Lógica del Tutorial ---
    # Lista de imágenes (asegúrate de definirlas en var.py)
    form['lista_imagenes'] = [
        var.IMG_TUTORIAL_1, 
        var.IMG_TUTORIAL_2, 
        var.IMG_TUTORIAL_3
    ]
    form['indice_actual'] = 0
    
    # Cargamos la primera imagen para mostrar
    path_inicial = form['lista_imagenes'][form['indice_actual']]
    form['img_tutorial'] = pg.image.load(path_inicial)
    form['img_tutorial'] = pg.transform.scale(form['img_tutorial'], (600, 400)) # Ajusta el tamaño

    
    form['btn_left'] = ButtonImage(
        x=100, y=var.DIMENSION_PANTALLA[1] // 2,
        text='', screen=form.get('screen'),
        image_path=var.IMG_BTN_LEFT, 
        width=50,   
        height=50,
        on_click=change_page, on_click_param={'form': form, 'direccion': -1}
    )

    # Botón Derecha (Siguiente)
    form['btn_right'] = ButtonImage(
        x=var.DIMENSION_PANTALLA[0] - 150, y=var.DIMENSION_PANTALLA[1] // 2,
        text='', screen=form.get('screen'),
        image_path=var.IMG_BTN_RIGHT, 
        width=50,   
        height=50,
        on_click=change_page, on_click_param={'form': form, 'direccion': 1}
    )


    form['btn_volver'] = ButtonImage(
        x=var.DIMENSION_PANTALLA[0] // 2 - 25, y=var.DIMENSION_PANTALLA[1] - 80,
        text='', screen=form.get('screen'),
        image_path=var.IMG_BTN_VOLVER,
        width=300,  
        height=70,
        on_click=base_form.set_active, on_click_param='form_menu'
    )

    var.dict_forms_status[form.get('name')] = form
    return form

def change_page(params: dict):
    """funcion el cual lleva a cabo change page.

    Args:
        params (tipo): descripcion del parametro params.

    """
    form = params.get('form')
    direccion = params.get('direccion')
    

    nuevo_indice = form['indice_actual'] + direccion
    

    if 0 <= nuevo_indice < len(form['lista_imagenes']):
        form['indice_actual'] = nuevo_indice
        path = form['lista_imagenes'][nuevo_indice]
        nueva_img = pg.image.load(path)
        form['img_tutorial'] = pg.transform.scale(nueva_img, (600, 400))
        print(f"Página actual: {form['indice_actual']}")

def draw(form_dict_data: dict):
    """funcion el cual lleva a cabo draw.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    screen = form_dict_data.get('screen')
    base_form.draw(form_dict_data)
    img = form_dict_data.get('img_tutorial')
    if img:
        rect_img = img.get_rect(center=(var.DIMENSION_PANTALLA[0]//2, var.DIMENSION_PANTALLA[1]//2))
        screen.blit(img, rect_img)
        
    form_dict_data['btn_left'].draw()
    form_dict_data['btn_right'].draw()
    form_dict_data['btn_volver'].draw()

def update(form_dict_data: dict):
    """funcion el cual lleva a cabo update.

    Args:
        form_dict_data (tipo): descripcion del parametro form_dict_data.

    """
    form_dict_data['btn_left'].update()
    form_dict_data['btn_right'].update()
    form_dict_data['btn_volver'].update()