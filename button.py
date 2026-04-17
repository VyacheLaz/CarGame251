import os
import pygame as pg



class Button:
    def __init__(self, asset_dir: str, asset_name: str, position: tuple[int]) -> None:
        self.default_image = pg.image.load(os.path.join(asset_dir, f'{asset_name}.png')).convert_alpha()
        self.hover_image = pg.image.load(os.path.join(asset_dir, f'{asset_name}_hover.png')).convert_alpha()
        self.button_rect = self.default_image.get_rect()
        self.x = position[0]
        self.y = position[1]
        self.is_hover = False
    
    def update_state(self) -> None:
        self.is_hover = not self.is_hover
        self.button_rect = (self.hover_image if self.is_hover else self.default_image).get_rect()

    
    def draw(self, screen) -> None:
        screen.blit(self.hover_image if self.is_hover else self.default_image, (self.x, self.y))