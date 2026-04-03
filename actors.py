import os
import pygame as pg
from random import choice
from config import ENEMY_IMAGES_DIR, PLAYER_SKINS_DIR
from config_manager import player_config


class PlayerCar:

    def __init__(self) -> None:
        self.image = pg.image.load(os.path.join(
            PLAYER_SKINS_DIR,
            f'{player_config.config["playerSkin"]}.png'
        )).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 260
        self.rect.y = 650
        self.rect.width = 64
        self.rect.height = 120
        self._speed = 1

    def render(self, screen) -> None:
        screen.blit(self.image, (self.rect.x,  self.rect.y))

    def move(self, state: list[int]) -> None:
        pressed_key = pg.key.get_pressed()
        if (pressed_key[pg.K_UP] or pressed_key[pg.K_w]) and self.rect.y > 0:
            self.rect.y -= self._speed
        if (pressed_key[pg.K_DOWN] or pressed_key[pg.K_s]) and self.rect.y < 660:
            self.rect.y += self._speed
        if (pressed_key[pg.K_LEFT] or pressed_key[pg.K_a]) and self.rect.x > 66:
            self.rect.x -= self._speed
        if (pressed_key[pg.K_RIGHT] or pressed_key[pg.K_d]) and self.rect.x < 463:
            self.rect.x += self._speed
        if pressed_key[pg.K_ESCAPE]:
            state[0] = 0
        pg.event.pump()


class EnemyCar:

    def __init__(self) -> None:
        self.image = pg.image.load(self.get_random_image()).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = choice([-600, -500, -650, -550, -800, -750, -800, -900, -100])
        self.rext_x = 0
        self.rect.width = 64
        self._speed = choice([1, 1.5, 2.5, 3, 2, 1.25])
        self.rect.height = 120

    @staticmethod
    def get_random_image() -> str:
        enemy_images = os.listdir(ENEMY_IMAGES_DIR)
        return os.path.join(ENEMY_IMAGES_DIR, choice(enemy_images))

    def render(self, screen) -> None:
        screen.blit(self.image, (self.rect.x,  self.rect.y))

    def move(self) -> None:
        self.rect.y += self._speed

