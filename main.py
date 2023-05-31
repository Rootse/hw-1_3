import random


class Engine():
    def __init__(self, m):
        self.__model = m
        self.__state = False

    def get_model(self):
        return self.__model

    def start(self, name):
        if self.__state:
            print(f"{name}/{self.__model} - The engine is already running")
            return

        print(f"{name}/{self.__model} - Engin started")

    def stop(self, name):
        if not self.__state:
            print(f"{name}/{self.__model} - The engine has already stopped")
            return

        print(f"{name}/{self.__model} - Stopping engine")


class Vehicle():
    def __init__(self, name, model, year, engin_model):
        self._name = name
        self._model = model
        self._year = year
        self._engin = Engine(engin_model)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def start(self):
        self._engin.start(self._name)

    def stop(self):
        self._engin.stop(self._name)

    def foo(self):
        print(f"Vehicle - {self._name}")


class Car(Vehicle):
    def __init__(self, name, model, year, engin_model):
        super().__init__(name, model, year, engin_model)
        self._num_wheels = 4

    def get_num_wheels(self):
        return self._num_wheels

    def set_num_wheels(self, num_wheels):
        self._num_wheels = num_wheels

    def honk(self):
        print(f"{self.get_name()} {self.get_model()} is honking.")

    def turn_on_lights(self):
        print(f"{self.get_name()} {self.get_model()} lights are on.")

    def turn_off_lights(self):
        print(f"{self.get_name()} {self.get_model()} lights are off.")

    def foo(self):
        print(f"Car - {self._name}")


class Helicopter(Vehicle):
    def __init__(self, name, model, year, engin_model):
        super().__init__(name, model, year, engin_model)
        self._max_altitude = 1000
        self._height = 0

    def get_max_altitude(self):
        return self._max_altitude

    def set_max_altitude(self, max_altitude):
        self._max_altitude = max_altitude

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height > self.get_max_altitude():
            print(f"The height cannot be higher than {self.get_max_altitude()}")
        elif height < 0:
            print(f"The height cannot be less than zero {self.get_max_altitude()}")

        self._height = height

    def land(self):
        print(f"{self.get_name()} {self.get_model()} is landing.")
        self.set_height(self.get_height() - 10)

    def hover(self):
        print(f"{self.get_name()} {self.get_model()} is hovering.")
        self.set_height(self.get_height() + 10)

    def foo(self):
        print(f"Helicopter - {self._name}")


# ---------------------- 4.1 ----------------------

print("# ---------------------- 4.1 ----------------------")
corolla = Car("Toyota Corolla", "Corolla", "2023", "1.6 L 4-cylinder")
corolla.start()

mi = Helicopter("MI-24", "MI-24", "2016", "Turboshaft")
mi.stop()
mi.start()

# ---------------------- 4.2 ----------------------

print("# ---------------------- 4.2 ----------------------")
array_obj = [random.choice([Car(f"car{i}", "n", "2023", "1.6 MPI"), Helicopter(f"car{i}", "n", "2023", "VK-2500")]) for
             i in range(500)]
for obj in array_obj:
    obj.foo()


# Каждый объект вызывает собственную переопределеную функию foo()


# ---------------------- 4.3 ----------------------


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows!")


def make_sound(animal):
    animal.sound()

print("# ---------------------- 4.3 ----------------------")
max = Dog("Max")
felix = Cat("Felix")

make_sound(max)
make_sound(felix)
