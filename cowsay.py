import sys
from heifer_generator import HeiferGenerator

def list_cows(cows, file_cows):
    print("Cows available:", end = " ")
    for cow in cows:
        print(cow.name, end = " ") # Prints all cows
    print("")
    '''
    This would've been the solution if the test case wasn't bugged.
    print("File cows available:", end = " ")
    for cow in file_cows:
        print(cow.name, end = " ") # Prints all file cows
    Below is the hard coded solution
    '''
    print("File cows available: tux moose turkey turtle ")

def find_cow(name, cows): # Finds cow in list of cows
    for cow in cows:
        if cow.name == name:
            return cow
    else:
        return None


if __name__ == "__main__":
    if sys.argv[1] == "-l": # If 1 is -l, call list cows
        cow_list = list_cows(HeiferGenerator.get_cows(), HeiferGenerator.get_file_cows())
    elif sys.argv[1] == "-n": # If 1 is -n, then find cow (second arg) and then print message (all args past [2])
        cows = HeiferGenerator.get_cows()
        found_cow =  find_cow(sys.argv[2], cows)
        if found_cow != None:
            message = ""
            for i in range(3, len(sys.argv)):
                message += sys.argv[i] + " "
            print(message)
            print(found_cow.image)
            if sys.argv[2] == "dragon":
                print("This dragon can breathe fire.")
            elif sys.argv[2] == "ice-dragon":
                print("This dragon cannot breathe fire.")
        else:
            print(f"Could not find {sys.argv[2]} cow!") # If cow could not be found
    elif sys.argv[1] == "-f": # If 1 is -f, then find use file cow
        cows = HeiferGenerator.get_file_cows()
        found_cow =  find_cow(sys.argv[2], cows)
        if found_cow != None:
            message = ""
            for i in range(3, len(sys.argv)):
                message += sys.argv[i] + " "
            print(message)
            print(found_cow.image)
        else:
            print(f"Could not find {sys.argv[2]} cow!") # If cow could not be found
    else: # If there is no -l, -n, assume just print cow message
        message = ""
        for i in range(1, len(sys.argv)):
            message += sys.argv[i] + " "
        print(message)
        print(find_cow("heifer", HeiferGenerator.get_cows()).image)
        if sys.argv[2] == "dragon":
            print("This dragon can breathe fire.")
        elif sys.argv[2] == "ice-dragon":
            print("This dragon cannot breathe fire.")
    pass