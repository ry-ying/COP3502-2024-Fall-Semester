from console_gfx import ConsoleGfx

'''
TEST CASES FOR 2B: Please ignore
    print("test cases:")
    print(to_hex_string([3,15,6,4]))

    print(count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]))
    print(count_runs([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))

    print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]))
    print(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]))
    print(encode_rle([1,2,3,4,1,2,3,4]))
    print(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    print(encode_rle([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

    print(get_decoded_length([3,15,6,4]))

    print(decode_rle([2,4,15,1,15,1,5,1,1,8,1,7]))
    print(decode_rle([3, 15, 6, 4]))

    print(string_to_data("3f64"))

'''



def to_hex_string(data): # Generic repetitive if/elif statement conversion to hex
    return_string = ""
    for value in data:
        if value >= 10:
            if value == 10:
                return_string = return_string + "a"
            elif value == 11:
                return_string = return_string + "b"
            elif value == 12:
                return_string = return_string + "c"
            elif value == 13:
                return_string = return_string + "d"
            elif value == 14:
                return_string = return_string + "e"
            elif value == 15:
                return_string = return_string + "f"
        else:
            return_string = return_string + str(value)
    return return_string


def count_runs(flat_data): # Checking if there is a number change or if the count of the current number has surpassed 15
    current_num = flat_data[0]
    count = 1
    runs = 1

    for value in flat_data[1:]:
        if value == current_num and count != 15:
            count += 1
        elif value != current_num or count == 15:
            runs += 1
            current_num = value
            count = 1
    return runs


def encode_rle(flat_data): # Essentially does the same as count_runs(), but instead appends the count and number that was counted into a list
    ret_data = []
    current_num = flat_data[0]
    count = 1

    for value in flat_data[1:]:
        if value == current_num and count != 15:
            count += 1
        elif value != current_num or count == 15:
            ret_data.extend([count, current_num])
            current_num = value
            count = 1
    ret_data.extend([count, current_num])

    return ret_data


def get_decoded_length(rle_data): # Basically cuts up into sections of two, takes the first index (number of occurrences) and adds them up
    length = 0
    for i in range(0, int((len(rle_data))/2)):
        length += rle_data[2*i]
    return length


def decode_rle(rle_data): # Does the same as above but multiplies the second index by the number of occurrences (first index)
    decoded = []
    for i in range(0, int((len(rle_data))/2)):
        decoded.extend([rle_data[2*i+1]]*(rle_data[2*i]))
    return decoded


def string_to_data(data_string): #Reverses hex to decimal
    ret_list = []
    for letter in data_string:
        if letter == "a":
            ret_list.append(10)
        elif letter == "b":
            ret_list.append(11)
        elif letter == "c":
            ret_list.append(12)
        elif letter == "d":
            ret_list.append(13)
        elif letter == "e":
            ret_list.append(14)
        elif letter == "f":
            ret_list.append(15)
        else:
            ret_list.append(int(letter))
    return ret_list


def to_rle_string(rle_data): # Converts string into hex, but adds a colon every 2 concatenations
    return_string = ""
    count = 0
    for value in rle_data:
        if value >= 10:
            count += 1
            if count % 2 == 0:
                if value == 10:
                    return_string = return_string + "a"
                elif value == 11:
                    return_string = return_string + "b"
                elif value == 12:
                    return_string = return_string + "c"
                elif value == 13:
                    return_string = return_string + "d"
                elif value == 14:
                    return_string = return_string + "e"
                elif value == 15:
                    return_string = return_string + "f"
            else:
                return_string = return_string + str(value)
        else:
            count += 1
            return_string = return_string + str(value)
        if count % 2 == 0 and count != 0 and count != len(rle_data):
            return_string = return_string + ":"

    return return_string


def string_to_rle(rle_string): # If/elif repetition heaven-- slices the entire string by each ":" and then appends the first character/second character
    split_string = rle_string.split(":")
    ret_list = []


    for splice in split_string:
        if len(splice) == 3:
            ret_list.append(int(splice[0:2]))
            if splice[2].isdigit():
                ret_list.append(int(splice[2]))
            else:
                if splice[2] == "a":
                    ret_list.append(10)
                elif splice[2] == "b":
                    ret_list.append(11)
                elif splice[2] == "c":
                    ret_list.append(12)
                elif splice[2] == "d":
                    ret_list.append(13)
                elif splice[2] == "e":
                    ret_list.append(14)
                elif splice[2] == "f":
                    ret_list.append(15)

        else:
            ret_list.append(int(splice[0]))
            if splice[1].isdigit():
                ret_list.append(int(splice[1]))
            else:
                if splice[1] == "a":
                    ret_list.append(10)
                elif splice[1] == "b":
                    ret_list.append(11)
                elif splice[1] == "c":
                    ret_list.append(12)
                elif splice[1] == "d":
                    ret_list.append(13)
                elif splice[1] == "e":
                    ret_list.append(14)
                elif splice[1] == "f":
                    ret_list.append(15)
    return ret_list


if __name__ == "__main__": #Main function
    print("Welcome to the RLE image encoder!")
    print("")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print("")
    image_data = None

    while True: # Loop to print menu and run commands
        print("")
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        print("")

        menu_option = int(input("Select a Menu Option: "))

        if menu_option == 1: # All the menu options
            filename = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(filename)

        elif menu_option == 2:
            print("Test image data loaded.")
            image_data = ConsoleGfx.test_image
        elif menu_option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))
        elif menu_option == 4:
            hex = (input("Enter the hex string holding RLE data: ")).lower()
            image_data = decode_rle(string_to_data(hex))
        elif menu_option == 5:
            hex_flat = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_flat)
        elif menu_option == 6:
            print("Displaying image...") # Have to check if image data is not none incase the user tries to run with empty data
            if image_data != None:
                ConsoleGfx.display_image(image_data)
            else:
                print("(no data)")
        elif menu_option == 7:
            if image_data != None:
                print("RLE representation: " + to_rle_string(encode_rle(image_data)))
            else:
                print("RLE representation: (no data)")
        elif menu_option == 8:
            if image_data != None:
                print("RLE hex values: " + to_hex_string(encode_rle(image_data)))
            else:
                print("RLE hex values: (no data)")
        elif menu_option == 9:
            if image_data != None:
                print("Flat hex values: " + to_hex_string(image_data))
            else:
                print("Flat hex values: (no data)")
        elif menu_option == 0:
            break
        else:
            print("Error! Invalid input.")
            pass



