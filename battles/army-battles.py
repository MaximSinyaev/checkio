#!/home/poligon/.local/bin/checkio --domain=py run army-battles

# 
# END_DESC

# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.hp = 50
        self.atc = 5
        self.is_alive = True
        
    def check_hp(self):
        self.is_alive = False if self.hp <= 0 else True

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.atc = 7

class Army():
    def __init__(self):
        self.army = list()
        self.last_alive = 0
        self.size = 0
        
    def add_units(self, unit_type, number):
        for i in range(number):
            self.army.append(unit_type())
        self.size += number

class Battle():
    def __init__(self):
        pass
        
    def fight(self, army1, army2):
        while (army1.army[army1.size - 1].is_alive &
               army2.army[army2.size - 1].is_alive):
            # print(army1.army[army1.last_alive], army2.army[army1.last_alive])
            # print(army1.last_alive, army2.last_alive)
            if self.duel(army1.army[army1.last_alive], army2.army[army2.last_alive]):
                #if army2.last_alive
                army2.last_alive += 1
            else:
                army1.last_alive += 1
        if army1.army[army1.size - 1].is_alive:
            return True
        return False
            
    @staticmethod
    def duel(unit_1, unit_2):
        while unit_1.is_alive and unit_2.is_alive:
            if unit_1.is_alive:
                unit_2.hp -= unit_1.atc
                unit_2.check_hp()
            if unit_2.is_alive:
                unit_1.hp -= unit_2.atc
                unit_1.check_hp()
        if unit_1.is_alive and not(unit_2.is_alive):
            return True
        return False


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.is_alive:
            unit_2.hp -= unit_1.atc
            unit_2.check_hp()
        
        if unit_2.is_alive:
            unit_1.hp -= unit_2.atc
            unit_1.check_hp()

    if unit_1.is_alive and not(unit_2.is_alive):
        return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")