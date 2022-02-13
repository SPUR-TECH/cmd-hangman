import random

print("LETS PLAY HANGMAN!!")
print("------------------------")


# No mistakes
def print_0_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 1 mistake
def print_1_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 2 mistakes
def print_2_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |      |  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 3 mistakes
def print_3_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 4 mistakes
def print_4_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 5 mistakes
def print_5_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     /   ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 6 mistakes
def print_6_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      0  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     / \\")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# function to print game status
def print_game_status():
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
        print(f"{element} ", end='')
    print(f"\nYou have {remaining_guesses} guess(es) left")


# Create list of words
words = ["hangman", "band", "house", "stereo", "tree", "swim", "creator"]

# Create alphabet
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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
print(word)

# Append an underscore for user to see as blank letter
for i in range(len(word)):
    guesses.append('_')

# Create game loop
game_over = False

while not game_over:
    print_game_status()

# Users guesses
    user_input = input("Please enter a letter:\n")
    letter = user_input.upper()
    used_letters += user_input.upper()
    print(f'"USED LETTERS:" {used_letters}')

# Display error message if not a letter
    if letter not in alphabet:
        print("Thats not a letter. Please try again")
    elif user_input in used_letters:
        print('"ALREADY USED!!"')
    else:
        # Display win message if all letters guessed
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
            if '_' not in guesses:
                print(f"YOU WIN!!! the word was '{word}'")
                game_over = True
        # Display try again message if letter not in word and
        #  lose message when all tries are used and end game
        else:
            print("sorry, try again")
            remaining_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                print_6_mistakes()
                print(f"You lose! the word was '{word}'")
                game_over = True

if __name__ == '__main__':
    while True:
        print("Do you want to play again?")
        print('Y/N')
        answer = input()
        if answer.lower == 'y':
            game_over = False
        if answer.lower == 'n':
            print("come back soon!!")
        break
