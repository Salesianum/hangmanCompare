from RunGame import play
from ChooseWord import Choose
#YOU SHOULD USE A WHILE LOOP TO GIVE YOUR GAME THE FOLLOWING:
#1. THE ABILITY TO PLAY THE GAME MORE THAN ONCE AT A TIME
#2. AFTER EACH GAME PROMPT THE USER "WOULD YOU LIKE TO PLAY AGAIN?"
#3. IF THE USER CHOOSES TO STOP PLAYING OUTPUT A WIN/LOSS RECORD (USE RUNGAME'S RETURN VALUE TO DETERMINE A VICTORY)

def main():
    #variables necessary to play
    secretWord = Choose()
    winOrLose = False
    continuePlay = True
    
    
    #run the game
    play()


if __name__ == "__main__":
    main()