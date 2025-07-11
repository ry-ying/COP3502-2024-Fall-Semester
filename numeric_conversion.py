def hex_char_decode(digit): #Cycles through every alphabetical A-F and assigns number
    if digit.isdigit():
        return int(digit)
    else:
        lower = digit.lower()
        if lower == "a":
            return 10
        elif lower == "b":
            return 11
        elif lower == "c":
            return 12
        elif lower == "d":
            return 13
        elif lower == "e":
            return 14
        elif lower == "f":
            return 15


def hex_char_encode(digit): #Performs reverse of hex_char_decode
    if digit < 10:
        return str(digit)
    elif digit == 10:
        return "A"
    elif digit == 11:
        return "B"
    elif digit == 12:
        return "C"
    elif digit == 13:
        return "D"
    elif digit == 14:
        return "E"
    elif digit == 15:
        return "F"


def hex_string_decode(hex): #Takes the string, checks if it starts with 0x, loops through each number to convert into decimal.
    total = 0
    start = 0
    index = 1
    if hex.startswith("0x"):
        start = 2
    for letter in hex[start:len(hex)]:
        total += hex_char_decode(letter) * (16 ** (len(hex) - start - index))
        index += 1
    return total


def binary_string_decode(binary): #Takes the string, checks if it starts with 0b, loops through each number to convert into decimal.
    total = 0
    start = 0
    index = 1
    if binary.startswith("0b"):
        start = 2
    for letter in binary[start:len(binary)]:
        if letter == "1":
            total += 2 ** (len(binary) - start - index)
        index += 1
    return total


def binary_to_hex(binary): # Was pretty difficult to do
    hexa = ""
    start = 0
    if binary.startswith("0b"):
        start = 2

    if (len(binary) - start) % 4 != 0: # Checking if the binary string is not divisible into equal sections of 4,
        index = 1
        total = 0
        for num in binary[start:(((len(binary) - start) % 4) + start)]: # Singles out the odd group and manually performs conversion
            if num == "1":
                total += 2 ** (((len(binary) - start) % 4) - index)
                index += 1
        hexa = hexa + hex_char_encode(total)
        start = start + (len(binary) - start) % 4

    for i in range(0, int((len(binary) - start) / 4)): # Takes the rest of the sections and performs conversion, concatenates the string onto hexa
        second_total = 0
        index = 1
        for num in binary[start + (i * 4):start + 4 + (i*4)]:
            if num == "1":
                second_total += 2 ** (4-index)
                index += 1
            else:
                index += 1

        hexa = hexa + hex_char_encode(second_total)

    return hexa


if __name__ == "__main__":
    #print(hex_string_decode("fFfFfFfF")) # Test cases to run through
    #print(hex_string_decode("0x4321"))
    #print(binary_string_decode("1010"))
    #print(binary_string_decode("0b11111111"))
    #print(binary_to_hex("011111111111"))
    while True: # Menu loop
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        print("")
        response = int(input("Please enter an option: "))

        if response == 1: # Each response starts a different function
            string = input("Please enter the numeric string to convert: ")
            print(f"Result: {hex_string_decode(string)}")
            print("")
        elif response == 2:
            string = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_string_decode(string)}")
            print("")
        elif response == 3:
            string = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_to_hex(string)}")
            print("")
        elif response == 4:
            print("Goodbye!")
            break
