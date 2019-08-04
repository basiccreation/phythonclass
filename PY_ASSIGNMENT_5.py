'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 5
Golf scores recording
---------------------

The program will give you the option to enter new golf players and their
golf scores

The program lets you retrieve the name of the pro and his average score
plus reminds the user what par is for golf.

The program saves the scores to golf.txt file but will ask the user to
enter the file they would like to open.

The program handles exceptions:

    IOError exceptions from the user entering the wrong name of the .txt file.

    ValueError exceptions that are raised when the items that are read from the
    file are converted to a number.
'''
# Global constant for pro player par score
PRO_PAR = 72

def main():
    
    
    print('\n\n---------------------')
    print('Golf Scores Recording')
    print('---------------------')
    userMenu()
#--------------------------------------------
'''
add_player_scores() asks for the number of player
user is adding and adds the player and their scores
to golf.txt
'''
def add_player_scores():
    # boolean variable to control loop
    another = "y"

    # Open golf.txt in append mode
    player_score_file = open("golf.txt", "a")

    # Add another player
    while another == "y" or another == "Y":
        # Get player name and scores
        print("----------------------------")
        print("Enter player name and scores")
        print("----------------------------\n")
        
        # Enter player name
        player_name = str(input("Enter name: "))

        # Add player name to golf.txt file
        player_score_file.write(player_name + "\n")
        
        # Promt user to enter number between 18 and 150
        print("Please enter the scores now. They should be between 18 and 150")
        
        # Loop through five scores to enter
        for count in range(1,6):
            playerscore = int(input(str(count)+". score:  "))
            
            # Ensuring player score is betwen 18 and 150
            while playerscore < 18 or playerscore > 150:
                print("Please enter a number between 18 and 150")
                playerscore = int(input(str(count)+". score:  "))

            # Add player score to golf.txt file
            player_score_file.write(str(playerscore) + "\n")
            
        # Ask if user wants to enter another
        another = input("Add another? (y) or (enter) to get to the menu \n>  ")

    # Close player_score_file
    player_score_file.close()
    print("The scores have been uploaded to golf.txt")

def read_player_scores():
    try:
        # Ask for file name to read
        file_name = input("Please enter file you would like to retrive.\n>  ")

        # Open golf.txt for reading
        read_player_score_file = open(file_name, 'r')

        # Read first player name
        player_name = read_player_score_file.readline()

        # If a field was read, continue reading the file
        while player_name != "":

            # Read the five scores
            score1 = int(read_player_score_file.readline())
            score2 = int(read_player_score_file.readline())
            score3 = int(read_player_score_file.readline())
            score4 = int(read_player_score_file.readline())
            score5 = int(read_player_score_file.readline())

            player_name = player_name.rstrip("\n")

            # Initialize accumulator for calculating average
            score_total = score1 + score2 + score3 + score4 + score5

            # Initalize average variable
            average = 0

            # Calculate average
            average = score_total / 5
                
            #Print player, scores and average
            print()
            print("Player name:\t", player_name)
            print("Average score:\t", average)

            player_name = read_player_score_file.readline()

        print("\n> Compare to the pro par:", PRO_PAR)      
        read_player_score_file.close()

    except IOError:
        print("\nAn error occoured trying to read the file.")
        print("Please check the file name.")

    except ValueError:
        print("\nNon-numeric data found in the file.")
        print("Please check the file after the above entry.")

    except:
        print("\nAn error accoured.")
        print("Please contact your administrator.")

        
def userMenu():
    program_open = "y" # Boolean variable, program is open until user closes 
    while program_open == "y":
        for menu_item in ["\nMenu",
                      "1. Enter New Player",
                      "2. Retrieve Player Data",
                      "3. Close Program"]:
            print(menu_item)

        # Get menu user selection
        try_again = ("\nPlease try again. Select a number between 1 and 3.\n> ")
        user_selection = int(input('\nWhat would you like to do? Please select:\n> '))

        # Check user selects a number between 1-5
        while user_selection < 0 or user_selection > 3:
            user_selection = int(input(try_again))

        # User menu functionality
        if (user_selection == 1):

            add_player_scores()
            
            # Show menu again so user can make another choice
            program_open = "y" 

        elif (user_selection == 2):
                
            read_player_scores()
            # Show menu again so user can make another choice
            program_open = "y"

        elif (user_selection == 3):
            print("\nClosing Program.\nGoodbye!\n\n")
            program_open = "n"
                
# Running Program
main()

'''
----------------------
OUTPUT
----------------------

====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_5.py ======


---------------------
Golf Scores Recording
---------------------

Menu
1. Enter New Player
2. Retrieve Player Data
3. Close Program

What would you like to do? Please select:
> 1
----------------------------
Enter player name and scores
----------------------------

Enter name: Kierkegaard S
Please enter the scores now. They should be between 18 and 150
1. score:  23
2. score:  56
3. score:  78
4. score:  34
5. score:  90
Add another? (y) or (enter) to get to the menu 
>  n
The scores have been uploaded to golf.txt

Menu
1. Enter New Player
2. Retrieve Player Data
3. Close Program

What would you like to do? Please select:
> 2
Please enter file you would like to retrive.
>  wrong file name

An error occoured trying to read the file.
Please check the file name.

Menu
1. Enter New Player
2. Retrieve Player Data
3. Close Program

What would you like to do? Please select:
> 2
Please enter file you would like to retrive.
>  golf.txt

Player name:	 Woods T
Average score:	 69.0

Player name:	 Johnson D
Average score:	 69.2

Player name:	 Koepka B
Average score:	 69.2

Non-numeric data found in the file.
Please check the file after the above entry.

Menu
1. Enter New Player
2. Retrieve Player Data
3. Close Program

What would you like to do? Please select:
> 2
Please enter file you would like to retrive.
>  golf.txt

Player name:	 Woods T
Average score:	 69.0

Player name:	 Johnson D
Average score:	 69.2

Player name:	 Koepka B
Average score:	 69.2

Player name:	 Schauffele X
Average score:	 69.2

Player name:	 Bjerregaard L
Average score:	 70.6

Player name:	 Kierkegaard S
Average score:	 56.2

> Compare to the pro par: 72

Menu
1. Enter New Player
2. Retrieve Player Data
3. Close Program

What would you like to do? Please select:
> 3

Closing Program.
Goodbye!


>>> 
'''





