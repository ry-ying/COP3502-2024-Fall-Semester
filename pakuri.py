class Pakuri():

    def __init__(self, species, attack=None, defense=None, speed=None): # Species built on the given project details
        self.species = species
        self.attack = (len(species)*7)+9
        self.defense = (len(species)*5)+17
        self.speed = (len(species)*6)+13

    def __gt__(self, other): # Necessary for the python sorting, since it cannot sort class instances
        return self.species > other.species

    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self): # evolution
        self.attack = self.attack*2
        self.defense = self.defense*4
        self.speed = self.speed*3