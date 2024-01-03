#contains all basic game information needed
#is the game manager. Call necessary functions and create all necessary variables.
#Ex, hangmanWord is an list. How do I add the correct number of underscores to it?
def play(secretWord):
    winOrLose = False
    lettersGuessed = []
    missesRemaining = 6
    guess = ""
    hangmanWord = []
    #Your Code Here
    hangmanWord = ["_"] * len(secretWord)
    continuePlaying = True
    #while the game isn't over (haven't won or lost loop)
    while(continuePlaying):
        display = createDisplayString(lettersGuessed, missesRemaining, hangmanWord)
        guess = handleUserInputLetterGuess(display, lettersGuessed)
        updater = processUserGuess(guess, secretWord, hangmanWord, missesRemaining)
        missesRemaining = updater[1]

        if (not "_" in hangmanWord):
            print(createDisplayString(lettersGuessed, missesRemaining, hangmanWord))
            return True
        if (missesRemaining == 0):
            return False

    return winOrLose


#EXAMPLE OF DISPLAY STRING:
#letters you've guessed: a e i o s u
#misses remaining: 4
#s _ _ _ o o _

#@PARAMS:
#lettersGuessed: a list of letters that have been previously guessed. 
#missesRemaining: a int that represents the number of guesses that are left.
#hangmanWord: A list of strings that represents the current progress in guessing the word.
#TODO USE THE PARAMS TO CREATE THE DISPLAY STRING SHOWN ABOVE.
def createDisplayString(lettersGuessed, missesRemaining, hangmanWord): 
    myDisplay = "\n\nLetters Guessed: "
    for letter in lettersGuessed:
        myDisplay += letter + " "
    myDisplay += f"\nMisses Remaining: {missesRemaining}\n"
    myDisplay += f"Word Progress: {hangmanWord}"

    return myDisplay

#PARAMETERS:
#lettersGuessed (type: list of strings) - a list of one character strings 
# where each is a letter that the user has already guessed
#displayString (type: string) - the value returned by createDisplayString
#TODO Print the displayString, 
#     Prompt a user guess and verify it is a valid guess, 
#     Add the guess to letters guessed
#     Return the valid guess as a string.
def handleUserInputLetterGuess(displayString, lettersGuessed):
    #your code here
    print(displayString)
    guess = input("Guess a Letter! ")
    while (not guess.isalpha() or len(guess) > 1 or guess in lettersGuessed):
        guess = input("Please enter a valid guess: ")
    lettersGuessed.append(guess)
    return guess



#PARAMS:
#   hangmanWord: 
#   guessedLetter:
#   secretWord: 

#PARAMS EXAMPLE:
#   guessedLetter = "a"
#   secretWord = "cat"
#   hangmanWord = ["c", "_", "_"]

#TODO returns the updated hangman word
#The new hangmanWord, which is a list of strings where each string is a single letter either corresponding
#to the same letter in secretWord or '_' if the user has not guessed the letter yet in the game.
def updateHangmanWord(hangmanWord, secretWord, guess):
    for index in range(len(secretWord)):
        if secretWord[index] == guess:
            hangmanWord[index] = guess
    
    



#Parameters:
#guessedLetter: (type: string) - the user's current guess, represented as a string of length 1, the return value of handleUserInputLetterGuess
#secretWord: (type: string) - the secret word returned by getWord
#hangmanWord: (type: list of strings) - represents the currently displayed hangman, each element in the list represents a letter in the secret word and it is either the actual letter or "_" representing that the user has not yet guessed that letter
#missesLeft: (type: int) - the number of misses the user has left

#Returns: Type: list
#A list with the following at each index:
#Index 0: (type: list of strings) the "new" hangmanWord based on the user's guess in guessedLetter, it should use the helper function updateHangmanWord to do this.
#Index 1: (type: int) an updated value for missesLeft based on the user's guess in guessedLetter
#Index 2: (type: bool) indication of whether the user made a correct guess, where True means the user guessed a letter in the word and False means the user missed

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesleft):
    list = []
    if guessedLetter in secretWord:
        updateHangmanWord(hangmanWord, secretWord, guessedLetter)
        list.append(hangmanWord)
        list.append(missesleft)
        list.append(True)
    else:
        list.append(hangmanWord)
        list.append(missesleft-1)
        list.append(False)  
    
    return list

