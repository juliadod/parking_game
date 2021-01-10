import pygame

from car import Car, State

import color


class CarView:

    def __init__(self, car, pos = [0, 0], car_width = 0):
        self.car = car
        self.x = pos[0]
        self.y = pos[1]
        self.car_width = car_width

        self.rect = None

        gap = 6

        if  self.car.state == State.UP:
            self.rect = pygame.Rect([self.x + gap,
                                     self.y + gap,
                                     car_width - gap * 2,
                                     car_width * self.car.length - gap * 2])

        elif self.car.state == State.RIGHT:
            self.rect = pygame.Rect([self.x - (self.car.length - 1) * car_width + gap,
                                     self.y + gap,
                                     car_width * self.car.length - gap * 2,
                                     car_width - gap * 2])

        elif self.car.state == State.DOWN:
            self.rect = pygame.Rect([self.x + gap,
                                     self.y - (self.car.length - 1) * car_width + gap,
                                     car_width - gap * 2,
                                     car_width * self.car.length - gap * 2])

        elif self.car.state == State.LEFT:

            self.rect = pygame.Rect([self.x + gap,
                                     self.y + gap,
                                     car_width * self.car.length - gap * 2,
                                     car_width - gap * 2])

    @property
    def state(self):
        return self.car.state


    def click(self, click_pos):
        x = click_pos[0]
        y = click_pos[1]

        rect = self.rect
        if rect.collidepoint([x, y]):
            return True
            """
            if y < rect.centery:
                if self.state == State.UP:   return "Head"
                if self.state == State.DOWN: return "Butt"

            if x < rect.centerx:
                if self.state == State.RIGHT: return "Head"
                if self.state == State.LEFT:  return "Butt"
            """

        return False


    def draw(self, surface):

        pygame.draw.rect(surface, color.ORANGE, self.rect)
