# Tt_Game война с "монстром" - рассказики для самых маленьких
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

class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon=None
        self.ename= None

    def changeEnemy(self, enemy):
        self.enemy = enemy
        print(f" Опасная встреча: {self.name} видит: приближается " +self.enemy.name)

    def changeWeapon(self, weapon):
        self.weapon = weapon
        str = f" Главное - не растеряться: {self.name} достает " +self.weapon.name_what
        print(str)
        return str


    def start(self):
        print("==> Начало:")
        print(f" Непобедимый боец {self.name} вступает в схватку!" )
        print(f" Противник сильный  -  {self.enemy.name} !" )

    def doAttack(self):
        print("==> Атака:")
        # print(f"2) weapon={self.weapon.name}")
        # s1 = self.weapon.attack()
        # print(f"3) weapon.atttack:  {self.weapon.attack()}")
        print(f" Боец {self.name} {self.weapon.attack()}")
        print(f" результат:  {self.enemy.name} {self.weapon.result()}")

    def end_fight(self):
        print("==> Заключение")
        print(f" Итог схватки: противник {self.enemy.name} {self.weapon.final()} ")
        print(f" Ура! {self.name} - победитель!")

class Monstr():
    def __init__(self, name):
        self.name = name

class Weapon_Knife(Weapon):
    def __init__(self, name, name_what):
        self.name = name
        self.name_what = name_what

    def attack(self):
        str = "наносисит страшный удар перочинным ножом"
        # print(str)
        return str

    def result(self):
        str = " сильно испугался"
        # print(str)
        return str

    def final(self):
        str = "быстро убежал"
        # print(str)
        return str

class Weapon_Rogatka (Weapon):
    def __init__(self, name, name_what):
        self.name = name
        self.name_what = name_what

    def attack(self):
        str = "стреляет из рогатки прямо в лоб!"
        # print(str)
        return str

    def result(self):
        str = " заплакал!"
        # print(str)
        return str

    def final(self):
        str = "запросил прощения"
        # print(str)
        return str

def story_fight(geroj, weapon, monstr):
    print(f"\n\n   Рассказ '{geroj.name} и {monstr.name}'")
    print(f" Герой нашей незамысловатой истории - {geroj.name}")
    geroj.changeEnemy(monstr)
    geroj.changeWeapon(weapon)
    geroj.start()
    geroj.doAttack()
    geroj.end_fight()

mon_gortnych = Monstr("змей Горыныч")
mon_hooligan = Monstr("хулиган Аболтусов")
mon_alkoholik = Monstr("пьяный мужик")

petja = Fighter("мальчик Петя")
galja = Fighter("смелая девочка Галя")

knife = Weapon_Knife("перочинный ножик", "перочинный ножик")
rogatka = Weapon_Rogatka("рогатка", "рогатку")

story_fight(petja, knife, mon_gortnych)
story_fight(petja, rogatka, mon_hooligan)
story_fight(galja, rogatka, mon_alkoholik)

