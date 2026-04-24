import os
import pygame as pg
from config import *


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


class RadioButton:
    def __init__(self, asset_dir: str,  position: tuple[int]) -> None:
        self.asset_image = pg.transform.scale(
            pg.image.load(asset_dir).convert_alpha(),
            (80 * 2, 128 * 2)
        )
        self.asset_rect = self.asset_image.get_rect()
        self.asset_rect.x = position[0] + 30
        self.asset_rect.y = position[1] + 30
        self.checked_sprite_image = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'Garage', 'checked.png')).convert_alpha()
        self.checked_rect = self.checked_sprite_image.get_rect()
        self.checked_rect.x = position[0]
        self.checked_rect.y = position[1]
        self.is_checked = False
    
    def draw(self, screen) -> None:
        screen.blit(self.asset_image, (self.asset_rect.x, self.asset_rect.y))
        if self.is_checked:
            screen.blit(self.checked_sprite_image, (self.checked_rect.x, self.checked_rect.y))
    