import random

def print_6_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     / \\")
    print(" /|\\")
    print("/ | \\")
    

# Create list of words 
words = ["hangman", "band", "house", "stereo", "tree", "swim",]
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


