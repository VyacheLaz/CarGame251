import pygame as pg
from actors import PlayerCar


def main() -> None:
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((600, 800))
    pg.display.set_caption("CarDriver")
    main_background1 = pg.image.load("Sources\\road_background.png")
    main_background2 = pg.image.load("Sources\\road_background.png")
    back_y1 = 0
    back_y2 = -800
    screen.blit(main_background1, (0, back_y1))
    screen.blit(main_background2, (0, back_y2))
    player_car = PlayerCar("Sources\\enemy.png")
    score_font = pg.font.SysFont("verdana", 15)
    score_value = 0
    speed_road = 4
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        player_car.move()
        back_y1 += speed_road
        back_y2 += speed_road
        screen.blit(main_background1, (0, back_y1))
        screen.blit(main_background2, (0, back_y2))
        if back_y1 == 800:
            back_y1 = -800
        if back_y2 == 800:
            back_y2 = -800
        score = score_font.render(
            f"Score: {int(score_value)}", 1, (255, 255, 0)
        )
        screen.blit(score, (0, 0))
        player_car.render(screen)
        pg.display.update()
        score_value += 0.02
    pg.quit()


if __name__ == '__main__':
    main()
