'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 6
World Series Champions
---------------------

This program returns a list of World Series winners to find a non-duplicated
list and then use that to determine how many times each team has won the World
Series.  We will also see which ones won the Series during each presidential
election from 1908 - 1992.

'''
# The programs main functions
def main():
    try:
        # Get list of winners from data file
        winners = readData()
        
        # Create list with no duplicate names and convert list to tuple
        winnersNDTuple = noDuplicates(winners)
        
        # Add up wins for all teams in a list and convert list to tuple
        numWinsTuple = numberWins( winners, winnersNDTuple )

        # Create a combined list from the two tuple with number of wins and team name
        createFileNoDuplicates( winnersNDTuple, numWinsTuple )

        '''
        ------------------------
        Attempt to append something to the wins tuple
        ------------------------
        '''
        #numWinsTuple.append(8)

        '''
        ------------------------
        Use the tuples in main() to print to the screen the same list
        that was just saved to the file
        ------------------------
        '''
        
        print("\nList of number of wins each team has had"+
              "\n----------------------------------------")
        
        # Loop through the teams in winnersNDTuple
        for team in winnersNDTuple:
            # Get team index in winnersNDTuple file
            team_index = winnersNDTuple.index(team)
            # Get number of wins with the team index from numWinsTuple file 
            num_wins = numWinsTuple[team_index]
            # Print number of wins, a tab divider, and team name to line variable
            print(str(num_wins)+"\t"+team)

        '''
        ------------------------
         Print out each team that won the World Series and the election year
         starting in 1908 and continuing to 1992 using the original winners list.
        ------------------------
        '''
        # Initialize year indexes for slicing
        # Subtract one extra due to no World Series in 1904
        index_of_1908 = 1908 - 1903 - 1 
        index_of_1992 = 1992 - 1903 - 1 + 1 # Add 1 to include 1992 in slice

        # Create list of winning teams in election years and the year the won
        winning_during_election_year_list = winners[index_of_1908:index_of_1992:4]      
        # Initialize indexes
        year_index = 1908
        list_index = 0

        print("\nList of teams winning during an election year " +
              "and the year they won"+
              "\n---------------------------------------------"+
              "---------------------")
        # Loop through winning_during_election_year_list,
        # Print team and year winning
        while list_index <= len(winning_during_election_year_list)-1:
            print(year_index,"\t",winning_during_election_year_list[list_index])
            year_index += 4
            list_index += 1


    except IOError:
        # Check for an IOError
        print("\nAn error occurred trying to read WorldSeriesWinnersND.txt.")
        print("Please check the file name.")
        
    except Exception as err:
        print("\nAn error occurred\n-----------------")
        print("ERROR: ",err,'\n\n')


# Read data from WorldSeriesWinners.txt 
def readData():
    
    # Initialize winner list variable
    original_full_list = [0]
    
    try:
        # Open WorldSeriesWinners.txt for reading
        wsw_file = open("WorldSeriesWinners.txt", 'r')
        
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
        print("\nAn error occurred trying to read WorldSeriesWinners.txt.")
        print("Please check the file name.")
        
    # Check for other errors
    except Exception as err:
        print("\nAn error occurred.\n------------------")
        print("ERROR: ",err,'\n\n')
                   
# Input list of winners created in readData and
# returns list of non-duplicate winners
def noDuplicates(winners):
    # Initialize list of no-duplicates
    no_dubs_list = []

    # Loop through winners list
    for team in winners:
        
        # Append non-duplicate winners to no_dubs_list
        if team not in no_dubs_list:
            no_dubs_list.append(team)

    # Convert list to a tuple
    no_dubs_tuple = tuple(no_dubs_list)
    
    # Return tuple to main()
    return no_dubs_tuple

# Input list from readData and tuple from noDuplicates
def numberWins( winners, winnersNDTuple ):

    # Initialize list of thennumber of wins
    wins_list = []

    # Create a list that holds the number of wins for each team
    # Loop through winnersNDTuple
    for team in winnersNDTuple:
        # Count wins in winners
        num_win = winners.count(team)
        # Add wins to wins_list
        wins_list.append(num_win)
        # Convert list to tuple
        wins_tuple = tuple(wins_list)
    # Return the tuple to the main
    return(wins_tuple)

# Input 2 tuples and prints them to WorldSeriesWinnersND.txt 
def createFileNoDuplicates( winnersNDTuple, numWinsTuple ):
    try:
        # Open WorldSeriesWinnersND.txt for writing
        file_with_no_duplicates = open("WorldSeriesWinnersND.txt", "w")
        
        # Loop through the teams in winnersNDTuple
        for team in winnersNDTuple:
            # Get team index in winnersNDTuple file
            team_index = winnersNDTuple.index(team)
            # Get number of wins with the team index from numWinsTuple file 
            num_wins = numWinsTuple[team_index]
            # Add number of wins, a tab divider, and team name to line variable
            line = (str(num_wins)+"\t"+team)
            
            # Write the line to file_with_no_duplicates
            file_with_no_duplicates.write(line+"\n")
        
        # Close file
        file_with_no_duplicates.close()
        
    except IOError:
        # Check for an IOError
        print("\nAn error occurred trying to read WorldSeriesWinnersND.txt.")
        print("Please check the file name.")
        
    except Exception as err:
        print("\nAn error occurred.\n------------------")
        print("ERROR: ",err,'\n\n')
         
main()

'''
------
OUTPUT
------
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_6.py ======

An error occurred
-----------------
ERROR:  'tuple' object has no attribute 'append' 


>>> 
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_6.py ======

List of number of wins each team has had
----------------------------------------
1	Boston Americans
5	New York Giants
3	Chicago White Sox
2	Chicago Cubs
5	Pittsburgh Pirates
5	Philadelphia Athletics
6	Boston Red Sox
1	Boston Braves
5	Cincinnati Reds
2	Cleveland Indians
26	New York Yankees
1	Washington Senators
10	St. Louis Cardinals
4	Detroit Tigers
1	Brooklyn Dodgers
1	Milwaukee Braves
5	Los Angeles Dodgers
3	Baltimore Orioles
2	New York Mets
4	Oakland Athletics
2	Philadelphia Phillies
1	Kansas City Royals
2	Minnesota Twins
2	Toronto Blue Jays
1	Atlanta Braves
2	Florida Marlins
1	Arizona Diamondbacks
1	Anaheim Angels

List of teams winning during an election year and the year they won
------------------------------------------------------------------
1908 	 Chicago Cubs
1912 	 Boston Red Sox
1916 	 Boston Red Sox
1920 	 Cleveland Indians
1924 	 Washington Senators
1928 	 New York Yankees
1932 	 New York Yankees
1936 	 New York Yankees
1940 	 Cincinnati Reds
1944 	 St. Louis Cardinals
1948 	 Cleveland Indians
1952 	 New York Yankees
1956 	 New York Yankees
1960 	 Pittsburgh Pirates
1964 	 St. Louis Cardinals
1968 	 Detroit Tigers
1972 	 Oakland Athletics
1976 	 Cincinnati Reds
1980 	 Philadelphia Phillies
1984 	 Detroit Tigers
1988 	 Los Angeles Dodgers
1992 	 Toronto Blue Jays
>>> 
'''
 
