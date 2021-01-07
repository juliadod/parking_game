import json
import pygame

from car import Car, State
from level import Level
from interface import Interface

car1 = Car("main", state = State.DOWN)
car2 = Car("car1", [1, 5])
car3 = Car("car2", [4, 8])
car4 = Car("car3", length = 3)
car5 = Car("car4", state = State.UP)

level = Level()

level.cars.append(car1)
level.cars.append(car2)
level.cars.append(car3)
level.cars.append(car4)
level.cars.append(car5)

out = open('level.json', 'w')

out.write(json.dumps(vars(level), indent = 4))

out.close()

input = open('level.json', 'r')

raw_data = input.read()

data = json.loads(raw_data)

loaded_level = Level.loadFromDict(data)

print(json.dumps(vars(loaded_level), indent = 4))

pygame.init()

size = [600, 600]
screen = pygame.display.set_mode(size, pygame.RESIZABLE, depth = 16)
pygame.display.set_caption("Парковка")

clock = pygame.time.Clock()

interface = Interface()

done = False
while not done:
    clock.tick(60)

    mouse = pygame.mouse.get_pressed()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.VIDEORESIZE:
            width, height = event.size

            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    screen.fill((255, 255, 255))

    interface.draw(screen)

    pygame.display.update()
