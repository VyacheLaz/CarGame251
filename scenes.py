import pygame as pg
from actors import EnemyCar


class GameScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.main_background1 = pg.image.load("Sources\\road_background.png")
        self.main_background2 = pg.image.load("Sources\\road_background.png")
        self.back_y1 = 0
        self.back_y2 = -800
        self.score_font = pg.font.SysFont("verdana", 15)
        self.score_value = 0
        self.speed_road = 4
        self._enemy_count = 4
        self._enemy_cars = self.get_enemy_cars()

    def get_enemy_cars(self) -> list:
        spawn_x = 50
        enemy_cars = []
        for _ in range(self._enemy_count):
            enemy_car = EnemyCar()
            enemy_car.x = spawn_x
            enemy_cars.append(enemy_car)
            spawn_x += 100
        return enemy_cars

    def move_enemy_cars(self) -> None:
        for i in range(self._enemy_count):
            enemy_car = self._enemy_cars[i]
            if enemy_car.y > 800:
                self._enemy_cars[i] = EnemyCar()
                self._enemy_cars[i].x = enemy_car.x
                self._enemy_cars[i].render(self.screen)
            else:
                enemy_car.move()
                enemy_car.render(self.screen)

    def render_scene(self) -> None:
        self.back_y1 += self.speed_road
        self.back_y2 += self.speed_road
        self.screen.blit(self.main_background1, (0, self.back_y1))
        self.screen.blit(self.main_background2, (0, self.back_y2))
        if self.back_y1 == 800:
            self.back_y1 = -800
        if self.back_y2 == 800:
            self.back_y2 = -800
        score = self.score_font.render(
            f"Score: {int(self.score_value)}", 1, (255, 255, 0)
        )
        self.move_enemy_cars()
        self.screen.blit(score, (0, 0))
        self.score_value += 0.02


class MainMenuScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load("Sources\\menu.png")

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))

