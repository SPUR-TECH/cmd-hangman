import random

def print_0_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_1_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_2_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |      |  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_3_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_4_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      0  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_5_mistakes():
    print("  |------|- ")
    print("  |      0  ")    
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     /   ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_6_mistakes():
    print("  |------|- ")
    print("  |      0  ")    
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     / \\")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")
    

def print_game_status():
    if mistakes == 0:
        print_0_mistakes()
        elif mistake == 1:
            print_1_mistakes()
        elif mistake == 2:
            print_2_mistakes()
        elif mistake == 3:
            print_3_mistakes()
        elif mistake == 4:
            print_4_mistakes()
        elif mistake == 5:
            print_5_mistakes()
        elif mistake == 6:
            print_6_mistakes()

# Create list of words 
words = ["hangman", "band", "house", "stereo", "tree", "swim", "creator"]
# Create letters tried
tries = []
# Lives tally
tries_left = 6
# Mistakes tally
mistakes = 0
# Randomize word selection
word_index = random.randint(0, len(words)-1)
word = words[word_index].upper()
print(word)

print_6_mistakes()
