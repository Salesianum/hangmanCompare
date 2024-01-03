from RunGame import play
from ChooseWord import Choose
#YOU SHOULD USE A WHILE LOOP TO GIVE YOUR GAME THE FOLLOWING:
#1. THE ABILITY TO PLAY THE GAME MORE THAN ONCE AT A TIME
#2. AFTER EACH GAME PROMPT THE USER "WOULD YOU LIKE TO PLAY AGAIN?"
#3. IF THE USER CHOOSES TO STOP PLAYING OUTPUT A WIN/LOSS RECORD (USE RUNGAME'S RETURN VALUE TO DETERMINE A VICTORY)

def main():
    #variables necessary to play
    winOrLose = False
    continuePlay = True
    wins = 0
    losses = 0
    #run the game
    while(continuePlay):
        secretWord = Choose()
        print(secretWord)
        if (play(secretWord) == False):
            losses += 1
        else:
            wins += 1
        answer = input("Would you like to play again? Y/N")
        while (not answer.isalpha()):
            answer = input("Please enter Y to play again or N to stop playing.... ")
        if answer != "Y":
            continuePlay = False

    print(f"\nYou won {wins} times and lost {losses} times... \nThanks for Playing!")


if __name__ == "__main__":
    main()