'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 8
World Series Champions (Round 2)
--------------------------------

The Program Spec:

    The user enters a year in the range of 1903 - 2008. And the
    program returns the winner of that year plus if they have
    more years than that.

'''
import pickle

# The programs main functions
def main():
    try:
        # Get list of winners from data file
        winners = readData()

        # Take winner list and make it into a dictionary
        yearD, winsD = makeDictionaries( winners )

        # Print non-duplicated winners to screen
        non_duplicated_winners = noDuplicates( yearD )
        print("\nHere's an alphabetized list of World Series winners")
        print("---------------------------------------------------")

        list_of_teams = []
        for team in non_duplicated_winners:
            list_of_teams.append(team)
        list_of_teams.sort()
        for team in list_of_teams:
            print(team)

        # Create the new file
        createFileNoDuplicates( winsD )
 
        print("\n--------------------------------")
        print("The World Series has been played")
        print("almost every year since 1903.")
        print("--------------------------------")
        print("Enter a year and we'll tell you")
        print("what team won the World Series")
        print("that year.")
        print("--------------------------------\n")

        

        # Initialize Boolean
        not_valid_year = True
        print("Enter the year you had in mind:")
        # Keep asking for a year until valid year is entered
        while not_valid_year == True:
            # Get year to look up
            year = input(">  ")

            # Error message if number is written with letters
            if not year.isdigit():
                print("Oops, that doesn't work.")
                print("Enter a year with numbers:")
            # Validate user input is in range 1903 - 2008
            elif int(year) < 1903:
                print("As mentioned, the World Series started in 1903.")
                print("Enter a different year:")
            # Validate user input is in range 1903 - 2008
            elif int(year) > 2008:
                print("Sorry, we only have data until 2008.")
                print("Enter a different year:")
            # Validate user input is digits
            elif year.isdigit():

                if int(year) == 1904 or int(year) == 2008:
                    print("Unfortunately there was no World Series in",year)
                    print("Goodbye!")
                else:
                    print()
                    print(year,"was a great year!\n----------------------")
                    winning_team = yearD.get(int(year))
                    print("The",winning_team,"won the World Series that year.")
                    years_won = winsD.get(winning_team)
                    if years_won == 1:
                        print("That's the only time",winning_team,
                              "won the World Series.")
                    elif years_won == 2:
                        print(winning_team,"has won the World Series twice.")
                    elif years_won == 3:
                         print(winning_team,"has won the World Series all of",
                               years_won,"times.")
                    else:
                        print("They have won the World Series a total of",
                              years_won,"times.")

    except IOError:
    # Check for an IOError
        print("\nHey, there was an error trying to read ")
        print("WorldSeriesWinnersND2.txt. Check the file name.")
            
    except Exception as err:
        print("\n--------------------------------")
        print("Oops, there's an error in main()")
        print("It says,",err,'\n\n')
        
'''-------------------------------------------------------
Reads data from WorldSeriesWinners2.txt and returns a list
-------------------------------------------------------'''
def readData():
    
    # Initialize winner list variable
    original_full_list = [0]
    
    try:
        # Open WorldSeriesWinners.txt for reading
        wsw_file = open("WorldSeriesWinners2.txt", 'r')
        
        # Read the file
        original_full_list = wsw_file.readlines()

        # Close WorldSeriesWinners.txt
        wsw_file.close()
            
        # Remove the end line characters
        index = 0
        
        # Loop through list and strip the new line character
        while index < len(original_full_list):
            original_full_list[index] = original_full_list[index].rstrip("\n")
            index += 1
 
        #Return the list to the main.
        return original_full_list
    
    # Check for an IOError
    except IOError:
        print("\nHey, there was an error trying to read ")
        print("WorldSeriesWinners2.txt. Check the file name.")
        
    # Check for other errors
    except Exception as err:
        print("\n------------------------------------")
        print("Oops, there's an error in readData()")
        print("It says,",err,'\n\n')
        
'''-----------------------------------------------
Takes the winners file and return two dictionaries
-----------------------------------------------'''

def makeDictionaries( winners ):

    # Initialize two dictionaries
    year_key_team_value_dic = {}
    team_key_win_value_dic = {}
    
    # Initialize first year World Series was played
    year_played = int(1903)
    
    # Initialize won games to 0
    games_won = int(0)
    
    for team in winners:

        '''
        Create dictionary
        with year as the key and
        team as the value.'''
        # Add year and team to year_key_team_value_dic
        year_key_team_value_dic[year_played] = team
        
        # Add one to the year_played counter
        year_played = int(year_played) + 1        
        
        '''
        Create dictionary 
        with team as the key and
        number of wins as the value.'''

        # Count wins in winners
        games_won = winners.count(team)

        # Add wins to team_key_win_value_dic
        team_key_win_value_dic[team] = games_won
    
    # Delete entry for year 1904
    year_key_team_value_dic.pop(1904,"entry not found")
    
    # Delete entry for year 1994
    year_key_team_value_dic.pop(1994,"entry not found")

    # Delete entries for no World Series Played in 1904 and 1994
    team_key_win_value_dic.pop("World Series Not Played in 1904","entry not found")
    team_key_win_value_dic.pop("World Series Not Played in 1994","entry not found")

    return year_key_team_value_dic, team_key_win_value_dic

'''----------------------------------------------------
Takes yearD and returns a set of non-duplicated winners
----------------------------------------------------'''
def noDuplicates( yearD ):
    # Initialize set
    no_dups_set = set()

    # Loop through yearD
    for team in yearD.values():
        # Add team name if it is not there
        if team not in no_dups_set:
            no_dups_set.add(team)

    # Return set to main()       
    return no_dups_set

'''---------------------------------------------------------------
Takes winsD and writes data to WorldSeriesWinnersND2.txt in binary
----------------------------------------------------------------'''
def createFileNoDuplicates( winsD ):

    try:
        # Open file for pickled data
        pickle_file = open("WorldSeriesWinnersND2.txt", "wb")
        # Write data to pickle_file
        pickle.dump(winsD, pickle_file)
        # Close pickle_file
        pickle_file.close()

    # Check for an IOError
    except IOError:
        print("\nHey, there was an error trying to read ")
        print("WorldSeriesWinnersND2.txt. Check the file name.")
        
    # Check for other errors
    except Exception as err:
        print("\n--------------------------------------------------")
        print("Oops, there's an error in createFileNoDuplicates()")
        print("It says,",err,'\n\n')    
    
main()
'''
------
OUTPUT
------

====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_8.py ======

Here's an alphabetized list of World Series winners
---------------------------------------------------
Anaheim Angels
Arizona Diamondbacks
Atlanta Braves
Baltimore Orioles
Boston Americans
Boston Braves
Boston Red Sox
Brooklyn Dodgers
Chicago Cubs
Chicago White Sox
Cincinnati Reds
Cleveland Indians
Detroit Tigers
Florida Marlins
Kansas City Royals
Los Angeles Dodgers
Milwaukee Braves
Minnesota Twins
New York Giants
New York Mets
New York Yankees
Oakland Athletics
Philadelphia Athletics
Philadelphia Phillies
Pittsburgh Pirates
St. Louis Cardinals
Toronto Blue Jays
Washington Senators

--------------------------------
The World Series has been played
almost every year since 1903.
--------------------------------
Enter a year and we'll tell you
what team won the World Series
that year.
--------------------------------

Enter the year you had in mind:
>  1903

1903 was a great year!
----------------------
The Boston Americans won the World Series that year.
That's the only time Boston Americans won the World Series.
>  
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_8.py ======

Here's an alphabetized list of World Series winners
---------------------------------------------------
Anaheim Angels
Arizona Diamondbacks
Atlanta Braves
...

--------------------------------
The World Series has been played
almost every year since 1903.
--------------------------------
Enter a year and we'll tell you
what team won the World Series
that year.
--------------------------------

Enter the year you had in mind:
>  1907

1907 was a great year!
----------------------
The Chicago Cubs won the World Series that year.
Chicago Cubs has won the World Series twice.
>  
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_8.py ======

Here's an alphabetized list of World Series winners
---------------------------------------------------
Anaheim Angels
Arizona Diamondbacks
Atlanta Braves
...

--------------------------------
The World Series has been played
almost every year since 1903.
--------------------------------
Enter a year and we'll tell you
what team won the World Series
that year.
--------------------------------

Enter the year you had in mind:
>  1906

1906 was a great year!
----------------------
The Chicago White Sox won the World Series that year.
Chicago White Sox has won the World Series all of 3 times.
>  
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_8.py ======

Here's an alphabetized list of World Series winners
---------------------------------------------------
Anaheim Angels
Arizona Diamondbacks
Atlanta Braves
...

--------------------------------
The World Series has been played
almost every year since 1903.
--------------------------------
Enter a year and we'll tell you
what team won the World Series
that year.
--------------------------------

Enter the year you had in mind:
>  1905

1905 was a great year!
----------------------
The New York Giants won the World Series that year.
They have won the World Series a total of 5 times.
>  
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_8.py ======

Here's an alphabetized list of World Series winners
---------------------------------------------------
Anaheim Angels
Arizona Diamondbacks
Atlanta Braves
...

--------------------------------
The World Series has been played
almost every year since 1903.
--------------------------------
Enter a year and we'll tell you
what team won the World Series
that year.
--------------------------------

Enter the year you had in mind:
>  four
Oops, that doesn't work.
Enter a year with numbers:
>  8000
Sorry, we only have data until 2008.
Enter a different year:
>  0
As mentioned, the World Series started in 1903.
Enter a different year:
>  1904
Unfortunately there was no World Series in 1904
Goodbye!
>  

'''
