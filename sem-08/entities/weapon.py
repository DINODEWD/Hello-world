from obj import Object

class Weapon(Object):
    def __init__(self, name, attack):
        super().__init__(name)
        self.attack = attack
        self.durability = 100
