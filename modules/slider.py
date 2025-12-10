import pygame as pg


class Slider:
    """
    Widget de barra deslizante (Slider) diseñado para interactuar con valores numéricos 
    como el volumen o la dificultad en una aplicación Pygame.

    Permite al usuario arrastrar un 'handle' (botón) para establecer un valor 
    dentro de un rango definido (mínimo a máximo).
    
        Inicializa el Slider con sus propiedades visuales y de valor.

        Args:
            pos (tuple): Coordenadas (X, Y) del centro del slider.
            size (tuple): Dimensiones (ancho, alto) de la barra contenedora.
            val_ini (float): Valor inicial del slider, debe estar entre min_val y max_val.
            min (int): Valor mínimo del rango que puede tomar el slider.
            max (int): Valor máximo del rango que puede tomar el slider.
            dragging (bool): indica si el usuario está actualmente arrastrando el botón (handle) del Slider con el ratón.
            progress_color (tuple): color de la barra de progreso.
            container_color (tuple): color de fondo de la barra.
            handle_color (tuple): color del boton el cual arrastra el usuario.
            
    """
    def __init__(self, pos: tuple, screen:object, size: tuple, val_ini: float, min: int, max: int, dragging = False, progress_color='blue', container_color='white', handle_color='red', on_change = None) -> None:
        self.pos = pos
        self.size = size
        self.current_value = val_ini
        self.screen = screen
        self.dragging = dragging
        self.progress_color = progress_color
        self.container_color = container_color
        self.handle_color = handle_color
        self.on_change = on_change
        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min 
        self.max = max


        self.container_rect = pg.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pg.Rect(self.slider_left_pos + self.current_value - 5, self.slider_top_pos, 10, self.size[1])

        range_val = self.max - self.min
        if range_val == 0:
            pixel_offset = 0
        else:
            pixel_offset = self.size[0] * ((self.current_value - self.min) / range_val)

        HANDLE_WIDTH = 20
        HANDLE_HEIGHT = self.size[1] + 20
        
        VERTICAL_SHIFT = (HANDLE_HEIGHT - self.size[1]) // 2 

        self.button_rect = pg.Rect(

            self.slider_left_pos + pixel_offset - (HANDLE_WIDTH // 2),
            

            self.slider_top_pos - VERTICAL_SHIFT, 
            
            HANDLE_WIDTH, 
            HANDLE_HEIGHT
        )

    def draw(self):

        pg.draw.rect(self.screen, self.container_color, self.container_rect)
        
        progress_width = self.button_rect.centerx - self.container_rect.left
        progress_rect = pg.Rect(self.container_rect.left, self.container_rect.top, progress_width, self.container_rect.height)
        
        pg.draw.rect(self.screen, self.progress_color, progress_rect)
        
        pg.draw.rect(self.screen, self.handle_color, self.button_rect)

    def handle_input(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.dragging = True
            elif self.container_rect.collidepoint(event.pos):
                self._update_value_from_pos(event.pos[0])
                self.dragging = True

        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == pg.MOUSEMOTION:
            if self.dragging:
                self._update_value_from_pos(event.pos[0])
                

    def _update_value_from_pos(self, mouse_x: int):
            
        limited_x = max(self.slider_left_pos, min(self.slider_right_pos, mouse_x))
            
            
        pixel_range = self.size[0]
        value_range = self.max - self.min
            

        offset_x = limited_x - self.slider_left_pos 
            
        new_value = self.min + (offset_x / pixel_range) * value_range
        self.current_value = round(new_value)
            
            
        self.button_rect.centerx = limited_x


        if self.on_change: 
            self.on_change(self.current_value)
        
    def get_value(self) -> int:
            return self.current_value
        
    def update(self):
            pass



        