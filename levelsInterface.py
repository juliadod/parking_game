"""import pygame

from color import *
from group import Group
from widget import Widget

class LevelsInterface:

    def __init__(self):

        self.game_info = Group(line_weight = 2, gap = 20,  text_scale_multiplier = 1.15, text_y_offset = -3)
        self.game_info.append(Widget(id = "level 1", weight = 1, text = "Уровень 1"))
        self.game_info.append(Widget(id = "level 2", weight = 1, text = "Уровень 2"))
        self.game_info.append("\n")
        self.game_info.append(Widget(id = "level 3", weight = 1, text = "Уровень 3"))
        self.game_info.append(Widget(id = "level 4", weight = 1, text = "Уровень 4"))
        self.game_info.append("\n")
        self.game_info.append(Widget(id = "level 5", weight = 1, text = "Уровень 5"))
        self.game_info.append(Widget(id = "level 6", weight = 1, text = "Уровень 6"))


    def draw(self, surface):
        self.game_info.draw(surface)


    def recalculate(self, window_size):
        self.game_info.width = window_size[0] * 0.8

        self.game_info.x = (window_size[0] - self.game_info.width) // 2

        self.game_info.y = window_size[1] * 0.2

        self.game_info.recalculate()


    def click(self, pos):
        for carView in self.car_views:
            if carView.click(pos):
                return carView

        return None
