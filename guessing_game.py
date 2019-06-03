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
 
    # gameplay variables      
    attempts = 0
    round = 1
    high_score = 0
    
    # function that 
    def greeting():
        print("")
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
        print("press [q] to quit")


    def magic_number_maker():
        """
        Generate and return a random integer between one and ten 
        inclusive.
        """
        magic_number = random.randint(1,10)
        return magic_number
    
    
    def set_high_score(attempts, high_score):
        """
        Set high_score to the lowest value of attempts and return 
        high_score.
        """
        if high_score == 0:
            return attempts
        elif attempts > high_score:
            return high_score
        elif attempts < high_score:
                return attempts
        else:
            return high_score
    

    def make_guess(round, attempts, high_score, magic_number):
        """
        Prompt user for an integer guess between 1 and 10 inclusive.
        If guess is correct, return number of attempts and prompt for 
        replay. Otherwise, continue prompting player for guess. 
        """
        while True:
            try:
                guess = input("Choose a number between 1 and 10: ")
                if guess == "q":
                    goodbye()
                if not guess.isdigit():
                    raise ValueError("Guess must be an integer value. " 
                                    "Please try again.")
                guess = int(guess)
                if guess > 10 or guess < 1:
                    raise ValueError("Guess is out of range. Please guess" 
                                    " between 1 and 10 inclusive.")
            except ValueError as err:
                print("Uh oh! {}".format(err))
            else:
                attempts += 1
                if guess == magic_number:
                    print("")
                    print("You guessed it! It took you {} attempt(s) to guess "
                        "the correct number!".format(attempts))
                    play_again(round, attempts, high_score)
                if guess > magic_number:
                    print("")
                    print("It's lower. Guess again!")
                    continue
                if guess < magic_number:
                    print("")
                    print("It's higher. Guess again!")
                    continue
    

    def play_again(round, attempts, high_score):
        """
        Prompt player for replay. Carry forward high_score into next 
        round. Generate new random integer and start new round.
        """
        while True:
            try:
                play_again = input("Play again? [y] or [n] ").lower()
                if play_again not in ("y","n","q"):
                    raise ValueError("Please enter the letter y or n.")
            except ValueError as err:
                print("Uh oh! {}".format(err))             
            else:    
                if play_again == "y":
                    round += 1
                    high_score = set_high_score(attempts, high_score)
                    attempts = 0
                    show_round(round, high_score)
                    magic_number = magic_number_maker()
                    make_guess(round, attempts, high_score, magic_number)
                else:
                    goodbye()
    
    
    def show_round(round, high_score):
        """
        Display round and high score to player.
        """
        print("\n")
        round_title_length = len(" Round {} ".format(round))
        top_border = int((35 - round_title_length) / 2)
        print("-" * top_border + " Round {} ".format(round) + "-" * top_border)
        if high_score:
            print(" ***** Current High Score: {} ***** ".format(high_score))
        else:
            print(" ***** Current High Score: NA ***** ")
        print("-" * 35)
    

    def goodbye():
        """
        Thank user for playing and exit.
        """
        print("")
        print("Thanks for playing! Goodbye!")
        print("")
        print("Credits:")
        print("Welcome banner generated at"
              " https://www.askapache.com/online-tools/figlet-ascii/")
        print("")
        exit()

    
    greeting()
    magic_number = magic_number_maker()
    show_round(round, high_score)
    make_guess(round, attempts, high_score, magic_number)
            

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    
    
    
    
    
