from pakuri import Pakuri

class Pakudex():

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.storage = []

    def get_size(self):
        return len(self.storage)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self): # Essentially cycle through all in storage, adds name to a list
        if len(self.storage) > 0:
            list = []
            for species in self.storage:
                list.append(species.species)
            return list
        else:
            return None

    def get_stats(self, species): # Cycles all species, if species is found then return a list with all data.
        for item in self.storage:
            if item.species == species:
                return [item.attack, item.defense, item.speed]
        else:
            return None

    def sort_pakuri(self):
        self.storage = sorted(self.storage)

    def add_pakuri(self, species): # Essentially looks through all the storage, and provides different outputs depending on whether or not species is found or is greater (failsafe)
        for pak in self.storage:
            if pak.species == species:
                return False
        self.storage.append(Pakuri(species))
        return True

    def evolve_species(self, species): # Cycles through all species, if the selected species is found then it will be evolved.
        for item in self.storage:
            if item.species == species:
                item.evolve()
                return True

        else:
            return False