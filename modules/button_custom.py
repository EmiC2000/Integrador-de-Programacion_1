import pygame as pg
from utn_fra.pygame_widgets.widget import Widget

class Button(Widget):
    def __init__(self, x, y, text, screen, font_path: str, align: str = 'center', color: tuple = (255,0,0), font_size = 25, on_click = None, on_click_param = None, outline_color: tuple = (0,0,0), outline_thickness = 0) -> None:
        super().__init__(x, y, text, screen, font_size)
        self.align = align
        self.color = color
        self.font = pg.font.Font(font_path, self.font_size)
        

        self.pos = (x, y) 
        self.outline_color = outline_color
        self.outline_thickness = outline_thickness if outline_thickness is not None else 0
        
        self.on_click = on_click
        self.on_click_param = on_click_param 
        

        self.render()

    def render(self) -> None:
        text_surface = self.font.render(self.text, True, self.color)
        
        if self.outline_thickness > 0 and self.outline_color is not None:
            thickness = self.outline_thickness
            outline_surface = self.font.render(self.text, True, self.outline_color)
            
            w = text_surface.get_width() + 2 * thickness
            h = text_surface.get_height() + 2 * thickness
            
            final_surface = pg.Surface((w, h), pg.SRCALPHA)
            
            center_x = thickness
            center_y = thickness
            
            for dx in range(-thickness, thickness + 1):
                for dy in range(-thickness, thickness + 1):
                    if dx != 0 or dy != 0:
                        final_surface.blit(outline_surface, (center_x + dx, center_y + dy))
            
            final_surface.blit(text_surface, (center_x, center_y))
            self.image = final_surface 
        else:
            self.image = text_surface

        self.rect = self.image.get_rect() 
        self.__set_align(self.pos) 

    def __set_align(self, coords: tuple):
        if self.align == 'topleft':
            self.rect.topleft = coords
        else:
            self.rect.center = coords

    def update_text(self, text: str, color: tuple = None) -> None:
        self.text = text
        if color:
            self.color = color
        self.render() 
        
    def button_pressed(self) -> None:
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.time.delay(300)
                if self.on_click:
                    self.on_click(self.on_click_param)
    
    def draw(self) -> None:
        # Usamos la pantalla del widget para dibujar
        self.screen.blit(self.image, self.rect)
    
    def update(self) -> None:
        self.draw()
        self.button_pressed()