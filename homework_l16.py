"""
Домашнее задание:

1. (Необязательно) Послушать "Научно-технический реп - Полиморфизм"

# Послушал. Забавно

2. (Обязательно) Реализовать классы и потомки по следующей схеме:

Класс Vehicle (средство передвижения).
У объектов класса Vehicle есть поля:
working_engine - с момента создания равно False, является обозначением того, заведен двигатель или нет

У объектов класса Vehicle есть методы:
start - выводит надпись "Двигатель заведен", если working_engine False и меняет его на True
move - выводит надпись "Средство передвижения едет", если working_engine True
stop - вывод надпись "Двигатель остановлен", если working_engine True и меняет его на False

У класса Vehicle есть потомки:
Tank - танк
Car - машина
Boat - надувная лодка

У объектов класса Tank есть поля:
count_ammo - с момента создания равно 10, боезапас танка

У объектов класса Tank есть методы:
move - выводит надпись "Гусиницы заскрипели от движения", если working_engine True, иначе выдаёт надпись "Нужно завести двигатель"
shoot - выводит надпись "Танк выстрелил" и уменьшает count_ammo на 1, если count_ammo > 0, иначе выдаёт надпись "Снаряды кончились"

У объектов класса Car есть поля:
fuel - с момента создания равно 100, топливо машины

У объектов класса Car есть методы:
start - выводит надпись "Двигатель машины заведён", если working_engine False, и меняет его на True. Если fuel <= 0, выдаёт надпись "Бензина нет"
move - выводит надпись "Машина поехала" и уменьшает fuel на 10, если working_engine True, иначе выдаёт надпись "Машина не заведена",
если fuel во время езды станет <= 0, тогда вывести надпись "Машина заглохла" и установить working_engine на False

У объектов класса Boat есть поля:
air_pressure - с момента создания равно 100, давление воздуха внутри лодки

У объектов класса Boat есть методы:
start - выводит надпись "Мотор лодки гудит", если working_engine False, и меняет его на True. Если если air_pressure <= 0, выдаёт надпись "Лодка тонет!" и двигатель не заводится
move - выводит надпись "Лодка плывёт", если working_engine True, и уменьшает air_pressure на 10, иначе выдаёт надпись "Мотор лодки не заведен"

Все объекты классов никаких дополнительных параметров на вход не получают, то есть их классы вызываются с пустыми скобками.
У классов-потомков только один родитель - Vehicle.
"""


class Vehicle:
    def __init__(self):
        self.working_engine = False

    def start(self):
        if not self.working_engine:
            self.working_engine = True
            print('Двигатель заведен')

    def move(self):
        if self.working_engine:
            print('Средство передвижения едет')

    def stop(self):
        if self.working_engine:
            self.working_engine = False
            print('Двигатель остановлен')


class Tank(Vehicle):
    def __init__(self):
        # не совсем разобрался для чего нужно вызывать инициализацию надкласса
        super().__init__()
        self.count_ammo = 10

    def move(self):
        if self.working_engine:
            print('Гусиницы заскрипели от движения')
        else:
            print('Нужно завести двигатель')

    def shoot(self):
        if self.count_ammo > 0:
            print('Танк выстрелил')
            self.count_ammo -= 1
        else:
            print('Снаряды кончились')


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel = 100

    def start(self):
        if self.fuel <= 0:
            print('Бензина нет')
        elif not self.working_engine:
            self.working_engine = True
            print('Двигатель машины заведён')

    def move(self):
        if not self.working_engine:
            print('Машина не заведена')
        # Добавил проверку на наличие бензина во время езды (не входило в задание)
        elif self.fuel <= 0:
            self.working_engine = False
            print('Машина заглохла')
        else:
            self.fuel -= 10
            print('Машина поехала')


class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        self.air_pressure = 100

    def start(self):
        if self.air_pressure <= 0:
            print('Лодка тонет!')
        elif not self.working_engine:
            self.working_engine = True
            print('Мотор лодки гудит')

    def move(self):
        # Добавил проверку на давление воздуха в лодке (не было в задании)
        if self.air_pressure <= 0:
            print('Лодка тонет!')
        elif not self.working_engine:
            print('Мотор лодки не заведен')
        else:
            self.air_pressure -= 10
            print('Лодка плывёт')


def main():
    tank1 = Tank()
    tank1.shoot()

    car1 = Car()
    car1.start()
    car1.move()

    boat1 = Boat()
    boat1.start()
    for _ in range(11):
        boat1.move()


if __name__ == '__main__':
    main()
