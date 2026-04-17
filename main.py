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
    game_over_scene = GameOverScene(screen)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if INTERFACE_STATE[0] == MAIN_MENU_STATE:
                    main_menu_scene.action(pg.mouse.get_pos())
                elif INTERFACE_STATE[0] == GAME_OVER_STATE:
                    INTERFACE_STATE[0] = MAIN_MENU_STATE
                    player_car = PlayerCar()
                    game_scene = GameScene(screen)
                    main_menu_scene = MainMenuScene(screen)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if INTERFACE_STATE[0] == MAIN_MENU_STATE:
                        INTERFACE_STATE[0] = GAME_STATE
                        game_scene.render_scene(player_car)
                        player_car.move()
                        player_car.render(screen)
                    elif INTERFACE_STATE[0] == GAME_OVER_STATE:
                        INTERFACE_STATE[0] = MAIN_MENU_STATE
                        player_car = PlayerCar()
                        main_menu_scene = MainMenuScene(screen)
                        game_scene = GameScene(screen)
            elif event.type == pg.QUIT:
                running = False
        if INTERFACE_STATE[0] == MAIN_MENU_STATE:
            main_menu_scene.mouse_hover(pg.mouse.get_pos())
            main_menu_scene.render_scene()
        elif INTERFACE_STATE[0] == GAME_STATE:
            game_scene.render_scene(player_car)
            player_car.move()
            player_car.render(screen)
        elif INTERFACE_STATE[0] == GAME_OVER_STATE:
            game_over_scene.render_scene()
        elif INTERFACE_STATE[0] == QUIT_STATE:
            running = False
        pg.display.update()
    pg.quit()


if __name__ == '__main__':
    main()
