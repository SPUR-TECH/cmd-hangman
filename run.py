import random


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
    print("  |      0  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 5 mistakes
def print_5_mistakes():
    print("  |------|- ")
    print("  |      0  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     /   ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")


# 6 mistakes
def print_6_mistakes():
    print("  |------|- ")
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

# Create letters tried
guesses = []

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

    user_input = input("Please enter a letter:\n")

    if not user_input:
        print("Thats not a letter. Please try again")
    else:
        letter = user_input.upper()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
            if '_' not in guesses:
                print(f"you win! the word was '{word}'")
                game_over = True
        else:
            print("sorry, try again")
            remaining_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                print_6_mistakes()
                print(f"You lose! the word was '{word}'")
                game_over = True
