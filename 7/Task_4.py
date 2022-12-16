"""Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат."""


class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Начало движения")

    def stop(self):
        print("Конец поездки")

    def tern(self, dirrection):
        print(f'поворот {dirrection}')

    def show_speed(self):
        print(f'Скорость :{self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        print(f'Скорость :{Car.speed}')


class SportCar(Car):
    is_polic = False


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        print(f'Скорость :{self.speed}')


class PoliceCar(Car):
    is_police = True


auto_1 = WorkCar(45, 'green', 'JSB')
print(auto_1.name)
auto_1.go()
auto_1.tern('left')
auto_1.show_speed()
auto_1.stop()

auto_2 = SportCar(150, 'yellow', 'Porsher')
print(auto_2.name)
auto_2.go()
auto_2.tern('left')
auto_2.show_speed()
auto_2.stop()

auto_3 = SportCar(55, 'Black', 'Hyndai')
print(auto_3.name)
auto_3.go()
auto_3.tern('right')
auto_3.show_speed()
auto_3.stop()
