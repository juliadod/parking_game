import pygame

class Cell:
    def __init__(self, size = [0, 0]):
        self.size = size


class Grid:

    def __init__(self, surface, size, level):
        self.size    = size

        self.__cells  = [0] * size[0]

        for i in range(size[0]):
            self.__cells[i] = [0] * size[1]

        for i in range(1, size[0]):
            for j in range(1, size[1]):
                self.__cells[i][j] = Cell(size)

        self.surface = surface
        self.level   = level

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, surface):
        self.__surface = surface

        cell_size = min(surface.get_size()) / min(self.size)

        for i in range(1, self.size[0]):
            for j in range(1, self.size[1]):
                self.__cells[i][j].size = cell_size


    def draw(self):
        cell_size = min(self.surface.get_size()) / min(self.size)
        cell_center = cell_size / 2

        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                obstacle = pygame.Rect(j*cell_size, i*cell_size, cell_size, cell_size)
                pygame.draw.rect(self.surface, (0, 0, 255), obstacle, 1)

        for i in level.cars:
            pass
