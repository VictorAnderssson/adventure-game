class Player:
    def __init__(self, hp, strength, lvl, inventory=[]):
        self.hp = hp
        self.strength = strength
        self.inventory = inventory
        self.lvl = lvl
            
            
    def change_hp(self, val):
        self.hp += val

    def change_strength(self, val):
        self.strength += val

    def change_level(self, val):
        self.lvl += val