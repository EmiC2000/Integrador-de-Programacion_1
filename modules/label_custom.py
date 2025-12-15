
import pygame as pg
from utn_fra.pygame_widgets.widget import Widget

class Label(Widget):
    '''
    This class represents any non interactable text seen on the screen  
    '''
    def __init__ (self,pos: tuple, text:str, screen:object, font_path: str, align: str = 'center', font_size:int = 50, color: tuple = (255,0,0), outline_color: tuple = None, outline_thickness: int = 0)->None:
        """
        This function initializes a text object with specified attributes such as position, text
        content, font style, and color on a screen.
        
        :param pos: display position object.
        :param text: The `text` parameter in the `__init__` method is a string that represents the text
        you want to display on the screen. This text will be rendered using the specified font and color
        onto the screen at the specified position (x, y)
        :param screen: The `screen` parameter in the `__init__` method is expected to be an object
        representing the display surface where the text will be rendered. This object is typically
        provided by a Pygame display window or screen object. It is used to render the text onto the
        screen using Pygame's font
        :param font_path: The `font_path` parameter in the `__init__` method is a string that represents
        the file path to the font file that will be used for rendering text. This font file is loaded
        using the `pg.font.Font` method to create a font object for rendering text in the specified font
        :param font_size: The `font_size` parameter in the `__init__` method is used to specify the size
        of the font that will be used to render the text on the screen. It is an optional parameter with
        a default value of 50 if not provided explicitly, defaults to 50
        :param color: The `color` parameter in the `__init__` method is a tuple that represents the RGB
        color values for the text that will be rendered. The default value for the `color` parameter is
        `(255, 0, 0)`, which corresponds to the color red in RGB format
        """
        self.x, self.y = pos
        self.pos = pos
        self.text = str(text) 
        

        super().__init__(self.x, self.y, self.text, screen, font_size)
        

        self.font = pg.font.Font(font_path, self.font_size)
        self.align = align
        self.color = color
        self.outline_color = outline_color
        self.outline_thickness = outline_thickness

        self.render_text()
    
    def __set_align(self, coords: tuple[int]):
        if self.align == 'topleft':
            self.rect.topleft = coords
        else:
            self.rect.center = coords

    def update_text(self, text: str, color: tuple[int,int,int]) -> None:
        """
        Actualiza el texto y el color de la fuente, y luego llama a render_text()
        para aplicar el texto, el color y el contorno (outline) si está configurado.
        """
        self.text = text
        self.color = color 
        
       
        self.render_text() 
        
        
        self.__set_align((self.x, self.y))
        
    def draw(self)->None:
        super().draw()

        self.screen.blit(self.image, self.rect)

    
    def update(self)->None:
        '''
        Executes the methods that need update 
        Arguments: None
        Returns: None
        '''
        self.draw()
    
    def render_text(self):
        
        text_surface = self.font.render(self.text, True, self.color)
        
        if self.outline_thickness > 0 and self.outline_color is not None:
            
            thickness = self.outline_thickness
            outline_surface = self.font.render(self.text, True, self.outline_color)
            
            w = text_surface.get_width() + 2 * thickness
            h = text_surface.get_height() + 2 * thickness
            
            final_surface = pg.Surface((w, h), pg.SRCALPHA)
            
            offsets = []
            for dx in range(-thickness, thickness + 1):
                for dy in range(-thickness, thickness + 1):
                    if dx != 0 or dy != 0:
                        offsets.append((dx, dy))
                        
            center_x = thickness
            center_y = thickness
            
            for dx, dy in offsets:
                final_surface.blit(outline_surface, (center_x + dx, center_y + dy))
                
            final_surface.blit(text_surface, (center_x, center_y))
            
            
            self.image = final_surface 

        else:
            self.image = text_surface
        
        self.rect = self.image.get_rect() 

        self.__set_align((self.pos))

    