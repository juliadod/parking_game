import pygame

from color import *
from group import Group
from widget import Widget
from level import Level
from car import Car, State
from carView import CarView

class GamePlayInterface:

    def __init__(self, level):
        self.level     = level
        self.car_views = []

        self.game_info = Group(line_weight = 3, text_scale_multiplier = 1.15, text_y_offset = -3)
        self.game_info.append(Widget(id = "Level name", weight = 1, text = level.name, clickable = False))
        self.game_info.append(Widget(id = "Steps",      weight = 1, text = "Шаги: "))
        self.game_info.append(Widget(id = "Best score", weight = 1, text = "Лучший: " + str(level.best_score)))

        self.game_field = Group(line_weight = level.map_width, gap = 0, square_buttons = True)

        for i in range(0, level.map_height):
            for j in range(0, level.map_width):
                self.game_field.append(Widget(id = str(i) + " " + str(j)))

            if i == level.exit_row:
                self.game_field.append(Widget(id = "exit"))

            self.game_field.append("\n")


    def draw(self, surface):

        self.game_info.draw(surface)
        self.game_field.draw(surface)

        for carView in self.car_views:
            carView.draw(surface)


    def recalculate(self, window_size):
        self.game_info.width = window_size[0] * 0.8

        self.game_info.x = (window_size[0] - self.game_info.width) // 2

        self.game_field.width  = window_size[0] * 0.8
        self.game_field.x = (window_size[0] - self.game_field.width) // 2
        self.game_field.y = window_size[1]  * 0.15

        self.game_info.recalculate()
        self.game_field.recalculate()

        self.car_views = []
        for car in self.level.cars:
            widget = self.game_field.get_widget_by_id(str(car.x) + " " + str(car.y))

            self.car_views.append(CarView(car,  [widget.x, widget.y], widget.width))



    def get_carView_rects(self):
        rects = []

        for carView in self.car_views:
            rects.append(carView.rect)

        return rects

    def clickCar(self, pos):
        for carView in self.car_views:
            if carView.click(pos):
                return carView

        return None
