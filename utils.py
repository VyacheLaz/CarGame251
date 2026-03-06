import pygame as pg
from config import GAME_NAME, ICON_WAY


def view_display() -> None:
    pg.init()
    pg.font.init()
    pg.display.set_caption(GAME_NAME)
    icon = pg.image.load(ICON_WAY)
    pg.display.set_icon(icon)
