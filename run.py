'''import necessary files'''
import random
from os import system


# No mistakes
def print_0_mistakes():
    '''Display first image with no mistakes'''
    # All the pieces of code with \u001b[--;1m are the colour changing codes
    # from www.lihaoyi.com
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 1 mistake
def print_1_mistakes():
    '''Display second image with one mistake'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1mo  ")
    print("\u001b[33;1m  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 2 mistakes
def print_2_mistakes():
    '''Display third image with two mistake'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1mo  ")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 3 mistakes
def print_3_mistakes():
    '''Display forth image with three mistake'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1mo  ")
    print("\u001b[33;1m  |     \u001b[31;1m/|  ")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 4 mistakes
def print_4_mistakes():
    '''Display fifth image with four mistake'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1mo  ")
    print("\u001b[33;1m  |     \u001b[31;1m/|\\")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 5 mistakes
def print_5_mistakes():
    '''Display sixth image with five mistakes'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1mo  ")
    print("\u001b[33;1m  |     \u001b[31;1m/|\\")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |     \u001b[31;1m/   ")
    print("\u001b[33;1m  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 6 mistakes
def print_6_mistakes():
    '''Display final image with all six mistakes'''
    print("\u001b[33;1m  |------|- ")
    print("  |      |  ")
    print("  |      \u001b[31;1m0  ")
    print("\u001b[33;1m  |     \u001b[31;1m/|\\")
    print("\u001b[33;1m  |      \u001b[31;1m|  ")
    print("\u001b[33;1m  |     \u001b[31;1m/ \\")
    print("\u001b[33;1m  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# function to print game status
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
        print(f"\u001b[32;1m{element} ", end='\u001b[37;1m')
    print(f"\nYou have {remaining_guesses} guess(es) left")


# Create game loop
def play_game():
    '''This is the main game loop and will continue till word is
     found or man is hung'''
    _ = system('clear')

    print("                                   ")
    print("                                   ")
    print("\u001b[37;1mLETS PLAY........")
    print("\u001b[32;1m                                   ")
    print("|    |    /\\    |\\    |    ---- |\\    /|    /\\    |\\    |  |")
    print("|    |   /  \\   | \\   |  /      | \\  / |   /  \\   | \\   |  |")
    print("|----|  /----\\  |  \\  | |   --- |  \\/  |  /----\\  |  \\  |  |")
    print("|    | /      \\ |   \\ | |     | |      | /      \\ |   \\ |    ")
    print("|    |/        \\|    \\|  \\____| |      |/        \\|    \\|  .")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("                                   ")
    print("                                   ")

    # Create list of words
    words = ["hangman", "band", "house", "stereo", "tree", "swim", "creator"
             "cheese", "doctor", "polite", "elephant", "river", "chair",
             "elevator", "worker", "climber", "coder"]

    # Create alphabet
    alphabet = ["A", "B", "C", "D", "E", "F",
                "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Zm"]

    # Create letters tried
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
        user_input = input("\u001b[37;1mPlease enter a letter:\n")
        letter = user_input.upper()

    # Display error message if not a letter
        if letter not in alphabet:
            print("\u001b[31;1mThats not a letter. Please try again")
        elif letter in used_letters:
            print('\u001b[31;1m"ALREADY USED!!"')
        else:
            used_letters += user_input.upper()
            print(f'"USED LETTERS:" \u001b[32;1m{used_letters}')
            # Display win message if all letters guessed
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guesses[i] = letter
                if '_' not in guesses:
                    print(f"\u001b[32;1mYOU WIN!!! the word was '{word}'")
                    game_over = True
            # Display try again message if letter not in word and
            #  lose message when all tries are used and end game
            else:
                print("\u001b[31;1m sorry, try again")
                remaining_guesses -= 1
                mistakes += 1
                if mistakes == 6:
                    print_6_mistakes()
                    print("\u001b[31;1m YOU LOSE!")
                    print(f"the word was \u001b[32;1m'{word}'\u001b[37;1m")
                    game_over = True

    menu()


def menu():
    '''This is the restart function'''
    print("\u001b[37;1mDo you want to play again?")
    print('\u001b[32;1mY/\u001b[31mN')
    answer = input()
    print(answer)
    if answer.upper() == 'Y':
        play_game()
    if answer.upper() == 'N':
        print("\u001b[32;1m COME BACK SOON!!!")


play_game()
