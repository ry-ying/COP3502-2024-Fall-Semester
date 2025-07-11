from p1_random import P1Random

rng = P1Random()

# Variables to store all the information throughout the game session
game_Active = True
games_Played = 0
games_Won = 0
games_Lost = 0
games_Tied = 0

while game_Active: # Loops while the player continues to play the game
    games_Played += 1
    print(f"START GAME #{games_Played}\n") # Prints out the game number.

    player_Hand = 0

    card = rng.next_int(13) + 1 # Creates randomly generated integer value 1,13 inclusive

    # Handles the first card deal, and adds it to the player's hand
    if card == 1:
        print("Your card is a ACE!")
        player_Hand += 1
    elif 2<= card <=10:
        print(f"Your card is a {card}!")
        player_Hand += card
    elif card == 11:
        player_Hand += 10
        print("Your card is a JACK!")
    elif card == 12:
        player_Hand += 10
        print("Your card is a QUEEN!")
    elif card == 13:
        player_Hand += 10
        print("Your card is a KING!")
    print(f"Your hand is: {player_Hand}\n") #Prints out hand value

    no_Winners = True
    while no_Winners: #Runs a loop while a game has not concluded/there is no winner to the current game

        menu = int(input("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: ")) #Opens the menu for the player
        print("\n", end = "")
        if menu == 1: #If player chooses 1, then it draws a random card and adds value to player's hand

            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                player_Hand += 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
                player_Hand += card
            elif card == 11:
                player_Hand += 10
                print("Your card is a JACK!")
            elif card == 12:
                player_Hand += 10
                print("Your card is a QUEEN!")
            elif card == 13:
                player_Hand += 10
                print("Your card is a KING!")
            print(f"Your hand is: {player_Hand}\n")

            #Checks if a player has a blackjack or has bust
            if player_Hand == 21:
                print("BLACKJACK! You win!\n")
                no_Winners = False
                games_Won += 1
            elif player_Hand > 21:
                print("You exceeded 21! You lose.\n")
                games_Lost += 1
                no_Winners = False
        elif menu == 2: #Draws for the dealer
            dealer_Hand = rng.next_int(11) + 16

            print(f"Dealer's hand: {dealer_Hand}")
            print(f"Your hand is: {player_Hand}\n")

            # Checks if the dealer's hand has bust or if the dealer's hand is greater than the players hand, or if
            # the dealer's hand is less than the player's hand, and if both hands are equal.
            # Adds the corresponding game statistic, then restarts the current game
            if dealer_Hand > 21:
                print("You win!\n")
                games_Won += 1
                no_Winners = False
            elif 21 >= dealer_Hand > player_Hand:
                print("Dealer wins!\n")
                games_Lost += 1
                no_Winners = False
            elif dealer_Hand < player_Hand:
                print("You win!\n")
                games_Won += 1
                no_Winners = False
            elif dealer_Hand == player_Hand:
                print("It's a tie! No one wins!\n")
                games_Tied += 1
                no_Winners = False
        elif menu == 3: #Provides statistics on the current game session
            print(f"Number of Player wins: {games_Won}")
            print(f"Number of Dealer wins: {games_Lost}")
            print(f"Number of tie games: {games_Tied}")
            print(f"Total # of games played is: {games_Played-1}")
            print(f"Percentage of Player wins: {round(games_Won*100/(games_Played-1),1)}%\n")
            #Finds percentage by multiplying games_Won divided by games_Played (minus one due to the current game)
            #then multiplied by 100 to get whole number and rounded to the first decimal.

        elif menu == 4: #Closes the game session
            no_Winners = False
            game_Active = False
        else:
            print("Invalid input!\nPlease enter an integer value between 1 and 4.\n") #Catches if user input is wrong




