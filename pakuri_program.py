from pakuri import Pakuri #Import all the classes
from pakudex import Pakudex


if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True: # Runs loop until a valid capacity is received (greater than 0 and not a text.)
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid size.")
            continue

    pakudex_inst = Pakudex(capacity) # Creates pakudex instance
    print(f"The Pakudex can hold {pakudex_inst.capacity} species of Pakuri.")

    while True: # Loops for the menu options

        print("")
        print("Pakudex Main Menu")
        print("-----------------")
        menu = """1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit"""
        print(menu)
        print("")


        try: # Same case as the capacity, loops until a valid menu selection is made
            option = int(input("What would you like to do? "))
            if option > 0 and option <= 6:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Unrecognized menu selection!")
            continue


        if option == 1: # Gets all species array, enumerates to make a list 1 to n
            if pakudex_inst.get_species_array():
                list = pakudex_inst.get_species_array()

                print("Pakuri In Pakudex:")
                for i,v in enumerate(list):
                    print(f"{i+1}. {v}")
            else:
                print("No Pakuri in Pakudex yet!")
        elif option == 2: # Uses get_stats and builds print output using the data list
            species_find = input("Enter the name of the species to display: ")
            species_inst = pakudex_inst.get_stats(species_find)
            if species_inst:
                print("")
                print(f"Species: {species_find}")
                print(f"Attack: {species_inst[0]}")
                print(f"Defense: {species_inst[1]}")
                print(f"Speed: {species_inst[2]}")
            else:
                print("Error: No such Pakuri!")
        elif option == 3: # A little iffy since I messed up the code here, but it would've detected the second parameter to determine the proper error message, else it is added to pakudex_inst.storage
            if len(pakudex_inst.storage) + 1 <= pakudex_inst.capacity:
                name_species = input("Enter the name of the species to add: ")
                species_inst = Pakuri(name_species)
                status = pakudex_inst.add_pakuri(name_species)
                if status == False:
                    print("Error: Pakudex already contains this species!")
                else:
                    print(f"Pakuri species {name_species} successfully added!")
            else:
                print("Error: Pakudex is full!")
        elif option == 4: # Uses evolve function to find species to evolve.
            name_evolve = input("Enter the name of the species to evolve: ")
            evolve_status = pakudex_inst.evolve_species(name_evolve)
            if evolve_status:
                print(f"{name_evolve} has evolved!")
            else:
                print("Error: No such Pakuri!")
        elif option == 5: # Sorts using built in python, and the adjusted __gt__ class funciton
            pakudex_inst.sort_pakuri()
            print("Pakuri have been sorted!")
        elif option == 6: # Closes program
            print("Thanks for using Pakudex! Bye!")
            break
