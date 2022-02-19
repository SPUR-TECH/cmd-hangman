# HANGMAN!!
https://cmd-hangman.herokuapp.com/

## Welcome reader,

In this section I will talk about the project and the issues and fixes that went into creating HANGMAN!

## Project mission:
---

The  aim of the project was to create a command line game in Python that accepts user input to progress through the game. with error messages on mistakes like wrong input type for instance numbers, spaces, symbols ETC. Even letters already used.

It also a restart option and  has a clear terminal function before restart to keep it clear for user ease.

I've added colour to it to keep the user entertained otherwise it may be a little boring to see a lot of single colour on the screen.

---

## START.....
![](images/hangman-start.png)

## END.....
![](images/hangman-end.png)


## Aim of the game:
---

The aim of the game is to guess the randomly selected word like traditional hangman without being hung. So you get 6 mistakes before it's too late. You wont lose a life on wrong input type or same letter twice..... I'm not that cruel. But you will obviously lose a life on wrong guesses and each time your wrong a piece of the man appears in the noose and you continue until you guess the word or hang....GOOD LUCK!


## features:
---

- You are first met with a message asking "Lets play....."
And underneath is a large title of HANGMAN handmade with keyboard symbols and tedious patience.

![](images/hangman-title.png)

- Then an empty gallows with random word ready for you to guess. Marked out with _ _ _ _ _ and a message saying "You have 6 guess(es) left".

![](images/hangman-empty.png)

- If you manage to guess every letter without mistakes you will only see used letters and the word appearing in the empty slots with the option to play again.

![](images/hangman-no-errors.png)

- If you guess incorrectly you will see parts of the man appearing in the gallows with a "Sorry try again" message and used letter list will build so you can always see what letter you've used.


![](images/hangman-used-letters.png)

- If you continue to guess incorrectly of course more of your man will appear and you will get a "YOU LOSE!" message and the word will be shown and you will get another chance to play again.

![](images/hangman-too-many-errors.png)

## Testing:
---

Debugging throughout the project was the first step to testing also due to the nature of the project things wont work unless you have no errors. I also ran the code through PEP8 and came back with no errors.

![](images/pep8-test.png)

## Bugs and fixes:
---

- BUG...Trying to create a list of used letters but each time a letter was guessed and added the "Already guessed" message appeared.
- FIX...I moved the error message further down the code away from add to used letters so a list built before error shows.

- BUG...creating a restart function.
- FIX...Place the actual game loop into a function then moving all the necessary parts of the code into the function.

- BUG...Colouring the code for the user caused everything after to turn that colour.
- FIX...Keep changing the colour on every section and after the section again.

- BUG...I have "try enumerating instead of iterating through range(len(word)).
- FIX Talk to Jo on tutor support and I was advised that it will be fine to keep the code as is.

## Credits:
---

- A big thank you to Jack mym mentor for helping me work out the used letter issue and restart issue and for everything else tht has made my coding journey easier.

- Many thanks to Jo for easing my mind on the enumerate issue and the package installation process for my project.

- Thanks to ANSI https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#16-colors  for adding colour to my code.

- Thanks to StudentEngineer for showing me that you can clear terminal on restart.

- Thanks to Stack overflow for explaining that I need double \ to show 1 \ in order to build the hangman images. 