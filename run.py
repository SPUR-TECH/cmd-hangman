'''import necessary files'''
import random
from os import system

# All the pieces of code with (\u001b[--;1m) are the colour changing codes
# from www.lihaoyi.com
GREEN = "\u001b[32;1m"
RED = "\u001b[31;1m"
YELLOW = "\u001b[33;1m"
WHITE = "\u001b[37;1m"


def print_0_mistakes():
    '''Display first image with no mistakes'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_1_mistakes():
    '''Display second image with one mistake'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}o  ")
    print(f"{YELLOW}  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_2_mistakes():
    '''Display third image with two mistake'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}o  ")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_3_mistakes():
    '''Display forth image with three mistake'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}o  ")
    print(f"{YELLOW}  |     {RED}/|  ")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_4_mistakes():
    '''Display fifth image with four mistake'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}o  ")
    print(f"{YELLOW}  |     {RED}/|\\")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_5_mistakes():
    '''Display sixth image with five mistakes'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}o  ")
    print(f"{YELLOW}  |     {RED}/|\\")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |     {RED}/   ")
    print(f"{YELLOW}  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_6_mistakes():
    '''Display final image with all six mistakes'''
    print(f"{YELLOW}  |------|- ")
    print("  |      |  ")
    print(f"  |      {RED}0  ")
    print(f"{YELLOW}  |     {RED}/|\\")
    print(f"{YELLOW}  |      {RED}|  ")
    print(f"{YELLOW}  |     {RED}/ \\")
    print(f"{YELLOW}  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


def print_game_status(mistakes, guesses, remaining_guesses):
    '''Call functions to display next image'''
    if mistakes == 0:
        print_0_mistakes()
    elif mistakes == 1:
        print_1_mistakes()
    elif mistakes == 2:
        print_2_mistakes()
    elif mistakes == 3:
        print_3_mistakes()
    elif mistakes == 4:
        print_4_mistakes()
    elif mistakes == 5:
        print_5_mistakes()
    elif mistakes == 6:
        print_6_mistakes()


# user input
    print("word: ", end='')
    for element in guesses:
        print(f"{GREEN}{element} ", end=f'{WHITE}')
    print(f"\nYou have {remaining_guesses} guess(es) left")


def play_game():
    '''This is the main game loop and will continue till word is
     found or man is hung'''
    _ = system('clear')

    print("                                   ")
    print("                                   ")
    print(f"{WHITE}LETS PLAY........")
    print(f"{GREEN}                                   ")
    print("|    |    /\\    |\\    |    ---- |\\    /|    /\\    |\\    |  |")
    print("|    |   /  \\   | \\   |  /      | \\  / |   /  \\   | \\   |  |")
    print("|----|  /----\\  |  \\  | |   --- |  \\/  |  /----\\  |  \\  |  |")
    print("|    | /      \\ |   \\ | |     | |      | /      \\ |   \\ |    ")
    print("|    |/        \\|    \\|  \\____| |      |/        \\|    \\|  .")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("                                   ")
    print("                                   ")

    # List of words randomly chosen
    words = ["hangman", "band", "house", "stereo", "tree", "swim", "creator"
             "cheese", "doctor", "polite", "elephant", "river", "chair",
             "elevator", "worker", "climber", "coder", "family", "broken"]

    # Alphabet to validate user input
    alphabet = ["A", "B", "C", "D", "E", "F",
                "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Z"]

    # Each letter of the word
    guesses = []

    # Create used letters
    used_letters = []

    # Guesses left
    remaining_guesses = 6

    # Mistakes made
    mistakes = 0

    # Randomize word selection
    word_index = random.randint(0, len(words)-1)
    word = words[word_index].upper()

    # Append an underscore for user to see as blank letter
    for i in range(len(word)):
        guesses.append('_')

    game_over = False
    while not game_over:
        print_game_status(mistakes, guesses, remaining_guesses)

    # Users guesses
        user_input = input(f"{WHITE}Please enter a letter:\n")
        letter = user_input.upper()

    # Display error message if not a letter
        if letter not in alphabet:
            print(f"{RED}Thats not a letter. Please try again")
        elif letter in used_letters:
            print(f'{RED}"ALREADY USED!!"')
        else:
            used_letters += user_input.upper()
            print(f'"USED LETTERS:" {GREEN}{used_letters}')
            # Display win message if all letters guessed
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guesses[i] = letter
                if '_' not in guesses:
                    print(f"{GREEN}YOU WIN!!! the word was '{word}'")
                    game_over = True
            # Display try again message if letter not in word and
            #  lose message when all tries are used and end game
            else:
                print(f"{RED} sorry, try again")
                remaining_guesses -= 1
                mistakes += 1
                if mistakes == 6:
                    print_6_mistakes()
                    print(f"{RED} YOU LOSE!")
                    print(f"the word was {GREEN}'{word}'{WHITE}")
                    game_over = True

    menu()


def menu():
    '''This is the restart function'''
    print(f"{WHITE}Do you want to play again?")
    print(f'{GREEN}Y/{RED}N')
    answer = input()
    print(answer)
    if answer.upper() == 'Y':
        play_game()
    if answer.upper() == 'N':
        print(f"{GREEN} COME BACK SOON!!!")


play_game()
