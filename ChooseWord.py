import random
#WRITE A FUNCTION TO READ THE CONTENTS OF THE WORDBANK.TXT
#FILE AND RANDOMLY SELECT ONE OF THE WORDS. 
#THE SELECTED WORD SHOULD BE RETURNED AND USED IN THE GAME.

#RETURNS THE CHOSEN STRING
def Choose():
    #Your code here
    selectedWord = random.choice(readFile());
    return selectedWord

#READ THE CONTENTS OF WORDBANK.TXT AND RETURN AN LIST
#OF STRINGS TO CHOOSE FROM.
def readFile():
    words = []
    with open("wordbank.txt") as file:
        while line := file.readline().rstrip("\n"):
            words.append(line)
    return words
