"""
Реализовать иерархию классов согласно приложенной UML-даиграмме.
Она описывает упрощенные элементы популярной игры Counter-Strike,
в которой команда контер-террористов пытается предотвратить планы
террористов.

Есть общий класс Person, от которого наследуются классы Terrorist
и CounterTerrorist. Помимо этого, есть класс Gun, от которого
наследуются AK и M4, каждый из которых состоит в отношении агрегации
соответственно игровой роли (АК для террористов, М4 для контер-террористов).

Реализации стрельбы и перезарядки для каждого класса остаются на усмотрение
разработчика. При желании что-то можно добавить.

В личный кабинет приложить .py файл с реализацией или же ссылку на github
репозиторий.
"""


class Person:
    def __init__(self, health):
        self.health = health

    def shoot(self):
        pass

    def reload(self):
        pass


class Terrorist(Person):
    def __init__(self, health, ak_gun):
        super().__init__(health)
        self.health = health
        self.gun = ak_gun  # Агрегация оружия при инициализации террориста

    # Определяю метод "shoot" для террориста
    def shoot(self, burst=3):
        print(f'Terrorist fires burst from the hip')
        for _ in range(burst):
            if self.gun.ammo == 0:
                print('The magazine is empty')
                break
            # использую метод "shoot" оружия
            self.gun.shoot()

    # Перезаряжаю оружие террориста
    def reload(self):
        # использую аттрибут класса AK74 "magazine_size"
        if self.gun.ammo == self.gun.magazine_size:
            print("Terrorist: Magazine is full")
        else:
            # использую метод родительского класса Gun "reload"
            self.gun.reload(self.gun.magazine_size)
            print('Terrorist: Ready to kill!')

    def __str__(self):
        return f"I'm a terrorist, my health is {self.health}% amd I have {self.gun}"


class CounterTerrorist(Person):

    def __init__(self, health, m4_gun):
        super().__init__(health)
        self.health = health
        self.gun = m4_gun

    def shoot(self, burst=2):
        print('Counter terrorist took aim and fired')
        for _ in range(burst):
            if self.gun.ammo == 0:
                print('The magazine is empty')
                break
            self.gun.shoot()

    def reload(self):
        if self.gun.ammo == self.gun.magazine_size:
            print("Counter terrorist: Don't shoot yet")
        else:
            self.gun.reload(self.gun.magazine_size)
            print('Counter terrorist: Reloaded!')

    def __str__(self):
        return f"I'm a counter terrorist, my health is {self.health}% and I have {self.gun}"


class Gun:
    def __init__(self, ammo):
        self.ammo = ammo

    def shoot(self):
        pass

    def reload(self, magazine_size):
        self.ammo = magazine_size


class AK(Gun):
    def __init__(self, ammo=40):
        super().__init__(ammo)
        self.magazine_size = 40
        self.ammo = ammo

    # Определяю метод одиночного выстрела
    def shoot(self):
        if self.ammo > 0:
            print('Bam ', end='')
            self.ammo -= 1

    def __str__(self):
        return f'AK-74 with {self.ammo} ammo'


class M4(Gun):
    def __init__(self, ammo=30):
        super().__init__(ammo)
        self.magazine_size = 30
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            print('Bah ', end='')
            self.ammo -= 1

    def __str__(self):
        return f'M4 machine gun with {self.ammo} ammo'


def main():
    ak_gun = AK()
    m4_gun = M4()

    initial_health = 100
    terrorist = Terrorist(initial_health, ak_gun)
    con_terrorist = CounterTerrorist(initial_health, m4_gun)

    print('Проверяю оружие:')
    print(ak_gun)
    print(m4_gun)
    print('\nОпрашиваю террориста и контр-террориста:')
    print(terrorist)
    print(con_terrorist)
    print('\nПробую перезарядить оружие у террориста:')
    terrorist.reload()
    print('\nТеррорист ведет беспорядочный огонь:')
    terrorist.shoot(35)
    print('\nТеррорист снова стреляет:')
    terrorist.shoot(10)
    print('\nКонт-террорист прицелился и стреляет:')
    con_terrorist.shoot()
    print('\n\nПроверяю оружие:')
    print(ak_gun)
    print(m4_gun)
    print('\nПерезаряжаю оружие:')
    con_terrorist.reload()
    terrorist.reload()
    print('\nПроверяю оружие контр-террориста:')
    print(m4_gun)


if __name__ == '__main__':
    main()
