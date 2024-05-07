class Car:
    def move(self):
        print('Car is moving...')

    def stop(self):
        print('Car is stopped')


my_car = Car()

my_car.move()
my_car.stop()

print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))
print(my_car.__dict__)

Car.move(my_car)
