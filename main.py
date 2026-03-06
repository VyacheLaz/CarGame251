from scenes import *
from actors import *
from config import *
from utils import view_display


def main() -> None:
    view_display()
    screen = pg.display.set_mode(SCREEN_SIZE)
    player_car = PlayerCar("Sources\\player.png")
    player_car.render(screen)
    game_scene = GameScene(screen)
    main_menu_scene = MainMenuScene(screen)
    running = True
    state = [0, ]
    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if state[0] == 0:
                    if pg.mouse.get_pos() > (124,240) and pg.mouse.get_pos() < (473, 327):
                        state[0] = 1
                    elif pg.mouse.get_pos() > (11, 729) and pg.mouse.get_pos() < (169, 789):
                        running = False
            elif event.type == pg.QUIT:
                running = False
        match state[0]:
            case 0:
                main_menu_scene.render_scene()
            case 1:
                game_scene.render_scene()
                player_car.move(state)
                player_car.render(screen)
        pg.display.update()
    pg.quit()


if __name__ == '__main__':
    main()
