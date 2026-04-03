from scenes import *
from actors import *
from config import *
from utils import view_display


def main() -> None:
    view_display()
    screen = pg.display.set_mode(SCREEN_SIZE)
    player_car = PlayerCar()
    player_car.render(screen)
    game_scene = GameScene(screen)
    main_menu_scene = MainMenuScene(screen)
    garage_scene = GarageScene(screen)
    settings_scene = SettingsScene(screen)
    game_over_scene = GameOverScene(screen)
    running = True
    state = [0, ]
    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if state[0] == 0:
                    if pg.mouse.get_pos() > (124,240) and pg.mouse.get_pos() < (473, 327):
                        state[0] = 1
                        player_car = PlayerCar()
                        game_scene = GameScene(screen)
                        main_menu_scene = MainMenuScene(screen)
                    elif pg.mouse.get_pos() > (11, 729) and pg.mouse.get_pos() < (169, 789):
                        running = False
                elif state[0] == -1:
                    player_car = PlayerCar()
                    main_menu_scene = MainMenuScene(screen)
                    state[0] = 0
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if state[0] == 0:
                        state[0] = 1
                        player_car = PlayerCar()
                        game_scene = GameScene(screen)
                        main_menu_scene = MainMenuScene(screen)
                    elif state[0] == -1:
                        player_car = PlayerCar()
                        main_menu_scene = MainMenuScene(screen)
                        state[0] = 0
            elif event.type == pg.QUIT:
                running = False
        if state[0] == 0:
            main_menu_scene.render_scene()
        elif state[0] == 1:
            game_scene.render_scene(player_car, state)
            player_car.move(state)
            player_car.render(screen)
        elif state[0] == -1:
            game_over_scene.render_scene()
        elif state[0] == 2:
            pass
        pg.display.update()
    pg.quit()


if __name__ == '__main__':
    main()
