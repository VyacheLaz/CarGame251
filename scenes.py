import os
import pygame as pg
from actors import EnemyCar
from config_manager import player_config
from config import *
from datetime import datetime
from button import Button, RadioButton


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
        self.score_font = pg.font.Font("Assets\\pixelFont.ttf", 36)
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

    def render_scene(self, player) -> None:
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
            f"Score: {int(self.score_value)}", 1, (0, 0, 0)
        )
        self.move_enemy_cars(player)
        if self.game_over:
            INTERFACE_STATE[0] = GAME_OVER_STATE
            return
        self.screen.blit(score, (0, 0))
        self.score_value += 0.02


class MainMenuScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'MainMenu\\Menu.png')).convert_alpha()
        self.start_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'MainMenu'), 'Start', (200, 250))
        self.garage_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'MainMenu'), 'Garage', (200, 380))
        self.scores_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'MainMenu'), 'Scores', (200, 510))
        self.quit_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'MainMenu'), 'Quit', (20, 700))


    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))
        self.start_button.draw(self.screen)
        self.garage_button.draw(self.screen)
        self.scores_button.draw(self.screen)
        self.quit_button.draw(self.screen)

    def action(self, mouse_pos: tuple[int]) -> None:
        if self.start_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = GAME_STATE
        elif self.quit_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = QUIT_STATE
        elif self.garage_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = GARAGE_STATE
    
    def mouse_hover(self, mouse_pos: tuple[int]) -> None:
        if self.start_button.button_rect.collidepoint(mouse_pos):
            self.start_button.update_state(True)
        elif self.garage_button.button_rect.collidepoint(mouse_pos):
            self.garage_button.update_state(True)
        elif self.scores_button.button_rect.collidepoint(mouse_pos):
            self.scores_button.update_state(True)
        elif self.quit_button.button_rect.collidepoint(mouse_pos):
            self.quit_button.update_state(True)
        else: 
            self.start_button.update_state(False)
            self.garage_button.update_state(False)
            self.scores_button.update_state(False)
            self.quit_button.update_state(False)


class GameOverScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'GameOver', 'GameOver_scene.png'))
        self.again_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'GameOver'), 'Again', (200, 600))
        self.back_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'GameOver'), 'Back', (20, 720))
        self.score_font = pg.font.Font("Assets\\pixelFont.ttf", 26)
        self.score_font = self.score_font.render(f'Your score: {player_config.config["lastScore"]}', 1, (0, 0, 0))

    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))
        self.screen.blit(self.score_font, (400, 700))
        self.again_button.draw(self.screen)
        self.back_button.draw(self.screen)

    def mouse_hover(self, mouse_pos: tuple[int]) -> None:
        if self.again_button.button_rect.collidepoint(mouse_pos):
            self.again_button.update_state(True)
        elif self.back_button.button_rect.collidepoint(mouse_pos):
            self.back_button.update_state(True)
        else:
            self.again_button.update_state(False)
            self.back_button.update_state(False)

    def action(self, mouse_pos: tuple[int]) -> None:
        if self.again_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = GAME_STATE
        elif self.back_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = MAIN_MENU_STATE



class GarageScene:
    def __init__(self, screen) -> None:
        self.screen = screen
        self._background = pg.image.load(os.path.join(INTERFACE_IMAGES_DIR, 'Garage', 'garage_scene.png'))
        self.default_car = RadioButton(os.path.join(PLAYER_SKINS_DIR, 'default.png'), (80, 80))
        self.blue_sky_car = RadioButton(os.path.join(PLAYER_SKINS_DIR, 'blueSky.png'), (300, 80))
        self.green_peace_car = RadioButton(os.path.join(PLAYER_SKINS_DIR, 'greenpeace.png'), (80, 400))
        self.purple_podonok_car = RadioButton(os.path.join(PLAYER_SKINS_DIR, 'purplePodonok.png'), (300, 400))
        self.back_button = Button(os.path.join(INTERFACE_IMAGES_DIR, 'Garage'), 'Back', (20, 720))
        self.get_current_skin()



    def render_scene(self) -> None:
        self.screen.blit(self._background, (0, 0))
        self.default_car.draw(self.screen)
        self.blue_sky_car.draw(self.screen)
        self.green_peace_car.draw(self.screen)
        self.purple_podonok_car.draw(self.screen)
        self.back_button.draw(self.screen)
    

    def get_current_skin(self) -> None:
        current_skin = player_config.config['playerSkin']
        if current_skin == 'purplePodonok':
            self.purple_podonok_car.is_checked = True
        elif current_skin == 'blueSky':
            self.blue_sky_car.is_checked = True
        elif current_skin == 'greenpeace':
            self.green_peace_car.is_checked = True
        else:
            self.default_car.is_checked = True
    
    def mouse_hover(self, mouse_pos: tuple[int]) -> None:
        if self.back_button.button_rect.collidepoint(mouse_pos):
            self.back_button.update_state(True)
        else:
            self.back_button.update_state(False)
    

    def action(self, mouse_pos: tuple[int]) -> None:
        if self.default_car.asset_rect.collidepoint(mouse_pos):
            self.default_car.is_checked = True
            self.blue_sky_car.is_checked = False
            self.green_peace_car.is_checked = False
            self.purple_podonok_car.is_checked = False
            player_config.change_setting('playerSkin', 'default')
        elif self.blue_sky_car.asset_rect.collidepoint(mouse_pos):
            self.blue_sky_car.is_checked = True
            self.default_car.is_checked = False
            self.green_peace_car.is_checked = False
            self.purple_podonok_car.is_checked = False
            player_config.change_setting('playerSkin', 'blueSky')
        elif self.green_peace_car.asset_rect.collidepoint(mouse_pos):
            self.green_peace_car.is_checked = True
            self.blue_sky_car.is_checked = False
            self.default_car.is_checked = False
            self.purple_podonok_car.is_checked = False
            player_config.change_setting('playerSkin', 'greenpeace')
        elif self.purple_podonok_car.asset_rect.collidepoint(mouse_pos):
            self.purple_podonok_car.is_checked = True
            self.green_peace_car.is_checked = False
            self.blue_sky_car.is_checked = False
            self.default_car.is_checked = False
            player_config.change_setting('playerSkin', 'purplePodonok')
        elif self.back_button.button_rect.collidepoint(mouse_pos):
            INTERFACE_STATE[0] = MAIN_MENU_STATE
    
