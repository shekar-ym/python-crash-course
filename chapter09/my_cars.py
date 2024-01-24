from car import Car
# from electric_car import ElectricCar as EC
import electric_car as EC


my_mustang = Car('ford','mustang','2022')
print(my_mustang.get_descriptive_name())


my_byd = EC.ElectricCar("byd", "dolphin", 2024)
print(my_byd.get_descriptive_name())
