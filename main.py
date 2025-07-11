def encode(password):
    encoded = ""
    for letter in password:
        encoded += str((int(letter) + 3) % 10) 
    return encoded


def decode(encoded_password):
    decoded = ""
    for letter in encoded_password:
        sub_int = int(letter)-3
        if sub_int < 0:
            sub_int += 10
        decoded = decoded + str(sub_int)
    return decoded


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        if option == 2:
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
                print("")
            else:
                print("No password has been encoded yet. Please try again.")

        elif option == 3:
            break
