# from car import Car,ElectricCar
import car

my_byd = car.ElectricCar("byd", "dolphin", 2024)
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()

my_mustang = car.Car('ford','mustang','2022')
print(my_mustang.get_descriptive_name())