import pygame as pg


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
        self.screen.blit(score, (0, 0))
        self.score_value += 0.02


class MainMenuScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load("Sources\\menu.png")

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))

