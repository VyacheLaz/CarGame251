import os
import pygame as pg



class Button:
    def __init__(self, asset_dir: str, asset_name: str, position: tuple[int]) -> None:
        self.default_image = pg.image.load(os.path.join(asset_dir, f'{asset_name}.png')).convert_alpha()
        self.hover_image = pg.image.load(os.path.join(asset_dir, f'{asset_name}_hover.png')).convert_alpha()
        self.button_rect = self.default_image.get_rect()
        self.button_rect.x = position[0]
        self.button_rect.y = position[1]
        self.is_hover = False
    
    def update_state(self, state: bool) -> None:
        self.is_hover = state
        x, y = self.button_rect.x, self.button_rect.y
        self.button_rect = (self.hover_image if self.is_hover else self.default_image).get_rect()
        self.button_rect.x = x
        self.button_rect.y = y

    
    def draw(self, screen) -> None:
        screen.blit(self.hover_image if self.is_hover else self.default_image, (self.button_rect.x, self.button_rect.y))