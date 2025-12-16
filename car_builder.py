from car import Car

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_gps(self, gps):
        self.car.gps = gps
        return self

    def build(self):
        return self.car
