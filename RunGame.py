#contains all basic game information needed
#is the game manager
def play():
    winOrLose = False
    #Your Code Here
    

    return winOrLose


#EXAMPLE OF DISPLAY STRING:
#letters you've guessed: a e i o s u
#misses remaining: 4
#s _ _ _ o o _

#@PARAMS:
#lettersGuessed: a list of letters that have been previously guessed. 
#missesRemaining: a int that represents the number of guesses that are left.
#hangmanWord: A string array that represents the current progress in guessing the word.
#TODO USE THE PARAMS TO CREATE THE DISPLAY STRING SHOWN ABOVE.
def createDisplayString(lettersGuessed, missesRemaining, hangmanWord):
    myDisplay = ""

    return myDisplay

#PARAMETERS:
#lettersGuessed (type: list of strings) - a list of one character strings 
# where each is a letter that the user has already guessed
#displayString (type: string) - the value returned by createDisplayString
#TODO Print the displayString, 
#     Prompt a user guess and verify it is a valid guess, 
#     Return the valid guess as a string.
def handleUserInputLetterGuess(displayString, lettersGuessed):

    guess = ""
    #your code here

    return 



#PARAMS:
#   hangmanWord: 
#   guessedLetter:
#   secretWord: 

#PARAMS EXAMPLE:
#guessedLetter = "a"
#   secretWord = "cat"
#   hangmanWord = ["c", "_", "_"]

#TODO returns the updated hangman word
#The new hangmanWord, which is a list of strings where each string is a single letter either corresponding
#to the same letter in secretWord or '_' if the user has not guessed the letter yet in the game.
def updateHangmanWord():

    return 



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

def processUserGuess():

    return

