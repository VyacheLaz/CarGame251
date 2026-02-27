import pygame as pg


class PlayerCar:

    def __init__(self, image_way: str) -> None:
        self.image = pg.image.load(image_way)
        self.rect = self.image.get_rect()
        self.x = 200
        self.speed = 1
        self.y = 600

    def render(self, screen) -> None:
        screen.blit(self.image, (self.x,  self.y))

    def move(self) -> None:
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP] and self.y > 0:
            self.y -= self.speed
        elif pressed_key[pg.K_DOWN] and self.y < 600:
            self.y += self.speed
        elif pressed_key[pg.K_LEFT] and self.x > 0:
            self.x -= self.speed
        elif pressed_key[pg.K_RIGHT] and self.x < 400:
            self.x += self.speed
        pg.event.pump()

