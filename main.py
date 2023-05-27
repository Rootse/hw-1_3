class Vehicle():
    def __init__(self, n, m, y):
        self._name = n
        self._model = m
        self._year = y

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


class Car(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self._num_wheels = 4

    def get_num_wheels(self):
        return self._num_wheels

    def set_num_wheels(self, num_wheels):
        self._num_wheels = num_wheels

    def honk(self):
        print(f"{self.get_name()} {self.get_model()} is honking.")

    def turn_on_lights(self):
        print(f"{self.get_make()} {self.get_model()} lights are on.")

    def turn_off_lights(self):
        print(f"{self.get_make()} {self.get_model()} lights are off.")


class Helicopter(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
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
