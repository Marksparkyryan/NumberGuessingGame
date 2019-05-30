"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you 
can totally do that by clicking: File -> Download Workspace in the file 
menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player 
      "It's lower".
      b. If the guess is less than the solution, display to the player 
      "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they 
    "Got it"
         and show how many attempts it took them to get the correct 
         number.
    5. Let the player know the game is ending, or something that 
    indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
          
    attempts = 0
    round = 1
    high_score = 0
    

    def greeting():
        print("Welcome to...")
        # Banner generated at 
        # https://www.askapache.com/online-tools/figlet-ascii/
        print("""        
  ________         _   __                __                           
 /_  __/ /_  ___  / | / /_  ______ ___  / /_  ___  _____
  / / / __ \/ _ \/  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
 / / / / / /  __/ /|  / /_/ / / / / / / /_/ /  __/ /  
/_/ /_/ /_/\___/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/    
                                                                                                                
   ______                     _             ______                   
  / ____/_  _____  __________(_)___  ____ _/ ____/___ _____ ___  ___ 
 / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/ / __/ __ `/ __ `__ \/ _ \\
/ /_/ / /_/ /  __(__  |__  ) / / / / /_/ / /_/ / /_/ / / / / / /  __/
\____/\__,_/\___/____/____/_/_/ /_/\__, /\____/\__,_/_/ /_/ /_/\___/ 
                                   /____/                                                                      
   """)
        if high_score:
            print("***** Current High Score: {} *****".format(high_score))
        print("-" * 35)
        print("~Round {}~".format(round))
    

    def magic_number_maker():
        magic_number = random.randint(1,10)
        return magic_number
    
    
    def set_high_score(attempts, high_score):
        if high_score == 0:
            return attempts
        elif attempts > high_score:
            return high_score
        elif attempts < high_score:
                return attempts
        else:
            return high_score

    
    magic_number = magic_number_maker()
    greeting()
    while True:
        try:
            guess = input("Choose a number between 1 and 10: ")
            if not guess.isdigit():
                raise ValueError("Guess must be an integer value. " 
                                 "Please try again.")
            guess = int(guess)
            if guess > 10 or guess < 1:
                raise ValueError("Guess is out of range. Please guess between " 
                                 "1 and 10.")
        except ValueError as err:
            print("Uh oh! {}".format(err))
        else:
            attempts += 1
            if guess == magic_number:
                print("You guessed it! It took you {} attempt(s) to guess "
                      "the correct number!".format(attempts))
                
                play_again = input("Play again? [y] or [n] ")
                if play_again == "y":
                    round += 1
                    high_score = set_high_score(attempts, high_score)
                    attempts = 0
                    print("\n")
                    print("~Round {}~".format(round))
                    print("***** Current High Score: "
                          "{} *****".format(high_score))
                    print("-" * 35)
                    magic_number = magic_number_maker()
                    continue
                else:
                    print("Thanks for playing! Goodbye!")
                    exit()
                    
            if guess > magic_number:
                print("It's lower. Guess again!")
                continue
            if guess < magic_number:
                print("It's higher. Guess again!")
                continue
                


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    
    
    
    
    
