# HeroicFight героическое сражение с "монстром" - рассказики для самых маленьких
# Демо-игра с абстрактными типами оружия и их реализацией

from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, name, name_what):
        self.name = name
        self.name_what = name_what

    @abstractmethod
    def attack(self):
        return ""

    @abstractmethod
    def result(self):
        return ""

    @abstractmethod
    def final(self):
        pass


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.enemy = None

    def change_enemy(self, enemy):
        self.enemy = enemy
        print(f" Опасная встреча: {self.name} видит: приближается " + self.enemy.name)

    def change_weapon(self, weapon):
        self.weapon = weapon
        s1 = f" Главное - не растеряться: {self.name} достает " + self.weapon.name_what
        print(s1)
        return s1

    def start(self):
        print("==> Начало:")
        print(f" Непобедимый боец {self.name} вступает в схватку!")
        print(f" Противник сильный  -  {self.enemy.name} !")

    def do_attack(self):
        print("==> Атака:")
        # print(f"2) weapon={self.weapon.name}")
        # s1 = self.weapon.attack()
        # print(f"3) weapon.attack:  {self.weapon.attack()}")
        print(f" Боец {self.name} {self.weapon.attack()}")
        print(f" результат:  {self.enemy.name} {self.weapon.result()}")

    def end_fight(self):
        print("==> Заключение")
        print(f" Итог схватки: противник {self.enemy.name} {self.weapon.final()} ")
        print(f" Ура! {self.name} - победитель!")


class Monster:
    def __init__(self, name):
        self.name = name


class WeaponKnife(Weapon):
    def __init__(self, name, name_what):
        super().__init__(name, name_what)
        self.name = name
        self.name_what = name_what

    def attack(self):
        s1 = "наносит страшный удар перочинным ножом"
        # print(s1)
        return s1

    def result(self):
        s1 = " сильно испугался"
        # print(s1)
        return s1

    def final(self):
        s1 = "быстро убежал"
        # print(s1)
        return s1


class WeaponSlingshot (Weapon):
    def __init__(self, name, name_what):
        super().__init__(name, name_what)
        self.name = name
        self.name_what = name_what

    def attack(self):
        s1 = "стреляет из рогатки прямо в лоб!"
        # print(s1)
        return s1

    def result(self):
        s1 = " заплакал!"
        # print(s1)
        return s1

    def final(self):
        s1 = "запросил прощения"
        # print(s1)
        return s1


def story_fight(hero, weapon, monster):
    print(f"\n\n   Рассказ '{hero.name} и {monster.name}'")
    print(f" Герой нашей незамысловатой истории - {hero.name}")
    hero.change_enemy(monster)
    hero.change_weapon(weapon)
    hero.start()
    hero.do_attack()
    hero.end_fight()


monster_gorynych = Monster("змей Горыныч")
monster_hooligan = Monster("хулиган Аболтусов")
monster_alcoholic = Monster("пьяный мужик")

petja = Fighter("мальчик Петя")
galja = Fighter("смелая девочка Галя")

knife = WeaponKnife("перочинный ножик", "перочинный ножик")
slingshot = WeaponSlingshot("рогатка", "рогатку")

story_fight(petja, knife, monster_gorynych)
story_fight(petja, slingshot, monster_hooligan)
story_fight(galja, slingshot, monster_alcoholic)
