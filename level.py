from car import Car

class Level:

    def __init__(self):
        self.cars       = []
        self.obstacles  = []
        self.best_score = 0

    @property
    def __dict__(self):
        serialised = {}

        serialised["best score"] = self.best_score

        cars = []
        for car in self.cars:
            cars.append(vars(car))

        serialised["cars"]       = cars
        serialised["obstacles"]  = self.obstacles

        return serialised


    def loadFromDict(source):
        level = Level()

        level.best_score = source["best score"]

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
