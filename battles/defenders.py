#!/home/poligon/.local/bin/checkio --domain=py run the-defenders

# 
# END_DESC

class Warrior():
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.df = 0
        self.is_alive = True

    def check_hp(self):
        self.is_alive = True if self.health > 0 else False


# class Rookie(Warrior):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.health = 50
#         self.attack = 1


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.health = 60
        self.attack = 3
        self.df = 2

class Army():
    def __init__(self):
        self.army = list()
        self.last_alive = 0
        self.size = 0

    def add_units(self, unit_type, number):
        for i in range(number):
            self.army.append(unit_type())
        self.size += number


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        # print(unit_1.hp, unit_2.hp)
        if unit_1.is_alive:
            unit_2.health -= (unit_1.attack - unit_2.df) if (unit_1.attack - unit_2.df) > 0\
                else 0
            unit_2.check_hp()
        # print(unit_1.health, unit_2.health)
        if unit_2.is_alive:
            unit_1.health -= (unit_2.attack - unit_1.df) if (unit_2.attack - unit_1.df) > 0\
                else 0
            unit_1.check_hp()
    # print("--" * 20)
    if unit_1.is_alive:
        return True
    return False


class Battle():
    def __init__(self):
        pass

    def fight(self, army1, army2):
        # print(">sizes", army1.size, army2.size)
        # print(">last_alive", army1.last_alive, army2.last_alive)
        while (army1.army[army1.size - 1].is_alive &
               army2.army[army2.size - 1].is_alive):
            if self.duel(army1.army[army1.last_alive], army2.army[army2.last_alive]):
                army2.last_alive += 1
            else:
                army1.last_alive += 1
        if army1.army[army1.size - 1].is_alive:
            return True
        return False

    @staticmethod
    def duel(unit_1: object, unit_2: object):
        return fight(unit_1, unit_2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    # print(chuck.is_alive)
    # chuck.hp = -123
    # print(chuck.is_alive)

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")