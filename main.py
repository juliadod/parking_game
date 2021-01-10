import json
import pygame

from car import Car, State
from level import Level
from gamePlayInterface import GamePlayInterface
from levelsInterface import LevelsInterface


car1 = Car("car1", [1, 0], 2, 1)
car2 = Car("car2", [0, 4], 3, 2)
car3 = Car("car3", [1, 5], 2, 3)
car4 = Car("car4", [4, 3], 3, 4)

level = Level("Уровень 1", 6, 6)

level.cars.append(car1)
level.cars.append(car2)
level.cars.append(car3)
level.cars.append(car4)

out = open('level.json', 'w')

out.write(json.dumps(vars(level), indent = 4))

out.close()

input = open('level.json', 'r')

raw_data = input.read()

data = json.loads(raw_data)

loaded_level = Level.loadFromDict(data)

pygame.init()

size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Парковка")

clock = pygame.time.Clock()


levels_interface = LevelsInterface()
levels_interface.recalculate(size)

game_interface = GamePlayInterface(loaded_level)
game_interface.recalculate(size)

selected_carView = None
done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_carView = game_interface.clickCar(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            selected_carView = None  # Отпускаем кнопку мыши - выбранной машины нет

        elif event.type == pygame.MOUSEMOTION:

            if selected_carView is not None:  # машина выбрана
                if event.buttons[0]:  # левая кнопка мыши нажата
                    # двигаем машинку
                    viewRect = selected_carView.rect
                    old_rect = viewRect.copy()


                    if selected_carView.state == State.UP or \
                       selected_carView.state == State.DOWN:

                       viewRect.y += event.rel[1]

                    if selected_carView.state == State.RIGHT or \
                       selected_carView.state == State.LEFT:

                       viewRect.x += event.rel[0]

                    viewRects = game_interface.get_carView_rects()

                    game_field_rect = game_interface.game_field.get_rect()

                    if not game_field_rect.contains(viewRect):
                        selected_carView.rect = old_rect

                    for rect in viewRects:
                        if rect != viewRect and \
                           rect.colliderect(viewRect):

                           selected_carView.rect = old_rect

                           

    screen.fill((0, 0, 0))

    levels_interface.draw(screen)

    pygame.display.update()
