import pygame as pg


class PlayerCar:

    def __init__(self, image_way: str) -> None:
        self.image = pg.image.load(image_way)
        self._rect = self.image.get_rect()
        self._x = 200
        self._speed = 1
        self._y = 600

    def render(self, screen) -> None:
        screen.blit(self.image, (self._x,  self._y))

    def move(self, state: list[int]) -> None:
        pressed_key = pg.key.get_pressed()
        if (pressed_key[pg.K_UP] or pressed_key[pg.K_w]) and self._y > 0:
            print(self._y)
            self._y -= self._speed
        if (pressed_key[pg.K_DOWN] or pressed_key[pg.K_s]) and self._y < 600:
            self._y += self._speed
        if (pressed_key[pg.K_LEFT] or pressed_key[pg.K_a]) and self._x > 0:
            self._x -= self._speed
        if (pressed_key[pg.K_RIGHT] or pressed_key[pg.K_d]) and self._x < 400:
            self._x += self._speed
        if pressed_key[pg.K_ESCAPE]:
            state[0] = 0
        pg.event.pump()

