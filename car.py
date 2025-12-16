class Car:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.color = None
        self.gps = None

    def specifications(self):
        print(f"Wheels: {self.wheels}, Engine: {self.engine}, Color: {self.color}, GPS: {self.gps}")
