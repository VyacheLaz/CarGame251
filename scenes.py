import os
import pygame as pg
from actors import EnemyCar
from config_manager import player_config
from config import INTERFACE_IMAGES_DIR
from datetime import datetime


class GameScene:
    '''
        Main game Scene
    '''
    def __init__(self, screen) -> None:
        self.screen = screen
        self.main_background1 = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'road_background.png'))
        self.main_background2 = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'road_background.png'))
        self.back_y1 = 0
        self.back_y2 = -800
        self.score_font = pg.font.SysFont("verdana", 15)
        self.score_value = 0
        self.speed_road = 4
        self._enemy_count = 6
        self._enemy_cars = self.get_enemy_cars()
        self.game_over = False

    def get_enemy_cars(self) -> list:
        '''
            Create enemy cars
        '''
        spawn_x = 60
        enemy_cars = []
        for _ in range(self._enemy_count):
            enemy_car = EnemyCar()
            enemy_car.rect.x = spawn_x
            enemy_cars.append(enemy_car)
            spawn_x += 75
        return enemy_cars

    def move_enemy_cars(self, player) -> None:
        '''
            Move enemy cars on road
        '''
        for i in range(self._enemy_count):
            enemy_car = self._enemy_cars[i]
            if player.rect.colliderect(enemy_car.rect):
                player_config.change_setting('lastScore', int(self.score_value))
                player_config.change_setting('lastScoreDate', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
                if self.score_value > player_config.config['bestScore']:
                    player_config.change_setting('bestScore', int(self.score_value))
                    player_config.change_setting('bestScoreDate', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
                self.game_over = True
                break
            if enemy_car.rect.y > 800:
                self._enemy_cars[i] = EnemyCar()
                self._enemy_cars[i].rect.x = enemy_car.rect.x
                self._enemy_cars[i].render(self.screen)
            else:
                enemy_car.move()
                enemy_car.render(self.screen)

    def render_scene(self, player, state: list[int]) -> None:
        '''
            Render main game scene
        '''
        self.back_y1 += self.speed_road
        self.back_y2 += self.speed_road
        self.screen.blit(self.main_background1, (0, self.back_y1))
        self.screen.blit(self.main_background2, (0, self.back_y2))
        if self.back_y1 >= 800:
            self.back_y1 -= 1600
        if self.back_y2 >= 800:
            self.back_y2 -= 1600
        score = self.score_font.render(
            f"Score: {int(self.score_value)}", 1, (255, 255, 0)
        )
        self.move_enemy_cars(player)
        if self.game_over:
            state[0] = -1
            return
        self.screen.blit(score, (0, 0))
        self.score_value += 0.02


class MainMenuScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'menu.png'))

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))

    def action(self) -> None:
        pass


class GameOverScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'GameOver.png'))

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))


class GarageScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'garage.png'))

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))


class SettingsScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'settings.png'))

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))


