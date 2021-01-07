from enum import IntEnum

class State(IntEnum):
    UP    = 1
    RIGHT = 2
    DOWN  = 3
    LEFT  = 4

class Car:

    def __init__(self, name = "noname", position = [0, 0], length = 0, state = State.UP):
        self.name   = name
        self.x      = position[0]
        self.y      = position[1]
        self.length = length
        self.state  = state


    @property
    def __dict__(self):
        serialised = {}

        serialised["name"]   = self.name
        serialised["x"]      = self.x
        serialised["y"]      = self.y
        serialised["length"] = self.length
        serialised["state"]  = int(self.state)

        return serialised
