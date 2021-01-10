from car import Car

class Level:

    def __init__(self, name = "", map_width = 0, map_height = 0, exit_row = 0):
        self.cars       = []
        self.obstacles  = []
        self.map_width  = map_width
        self.map_height = map_height
        self.name       = name
        self.best_score = 0
        self.exit_row   = exit_row

    @property
    def __dict__(self):
        serialised = {}

        serialised["name"]       = self.name
        serialised["best score"] = self.best_score
        serialised["exit row"]   = self.exit_row
        serialised["map width"]  = self.map_width
        serialised["map height"] = self.map_height

        cars = []
        for car in self.cars:
            cars.append(vars(car))

        serialised["cars"]       = cars
        serialised["obstacles"]  = self.obstacles

        return serialised


    def loadFromDict(source):
        level = Level()

        level.name       = source["name"]
        level.best_score = source["best score"]
        level.exit_row   = source["exit row"]
        level.map_width  = source["map width"]
        level.map_height = source["map height"]

        for car in source["cars"]:
            level.cars.append(Car(car["name"],
                                  (car["x"], car["y"]),
                                  car["length"],
                                  car["state"]))

        for obstacle in source["obstacles"]:
            level.cars.append(Car(car["name"],
                                  (car["x"], car["y"]),
                                  car["length"],
                                  car["state"]))

        return level
