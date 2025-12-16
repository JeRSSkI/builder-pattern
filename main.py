from car_builder import CarBuilder

builder = CarBuilder()
car = (
    builder
    .set_wheels(4)
    .set_engine("V8")
    .set_color("Red")
    .set_gps(True)
    .build()
)

car.specifications()
