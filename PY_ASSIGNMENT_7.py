'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 7
Word Games
---------------------

The Program Spec

The user is asked to enter a string of minimum of 3 words.  
Then returns three things:

    The target string with the Pig Latin change.
    The target string with the Turkey Irish change.
    The number of vowels in the target string.

order of operations:

Everything is done from main().

The program should loop for a total of 3 times asking the user for a string each time.

Input function

    getString()
    This function requests a string from the user and converts it to a list to be able to see how many words were entered.  Use a validation loop to get the minimum of 3 words (use a constant for this minimum).  Return the targetList to the main()

Processing functions

    pigLatin( targetList )
    This function will receive the list of words as an argument and returns a new string that has moved the first letter to the end and added "ay" to each word in the targetList. Start by making each word all lower case for consistency.  Consider slicing the word to get certain parts and then create the new string.

    turkeyIrish( targetList )
    This function will receive the list of words as an argument and returns a new string that has "ab" added before each vowel in each word. Start by making each word all lower case for ease in searching for vowels ('a', 'e', 'i', 'o', 'u') in the words.  Think about how look at each letter and then add to the new string. 

    countVowels( targetList )
    This function will receive the list of words as an argument and returns the number of vowels that appear in the list of words.  Check for 'a', 'e', 'i', 'o', 'u'.  Again think about making the words lower case to help with the search.

Input Errors
    Whenever the user makes an input error, keep at them until they get it right. 
    Do not allow them out of the validation loop until you have acquired a legal value, 
    even if it takes years . . .   :)

Test Run Requirements:

Have the program loop for a total of 3 times asking the user for a string each time.  
In at least one of the three, intentionally commit input errors like less than 3 words 
to demonstrate the illegal input.  Be sure to include comments in your code.

'''
# Constant for number of games is set to 3 individual games
MAX_GAMES = 3 
        
# The programs main functions
def main():
    gameCount = 0 # initialize gameCount to 0

    # Welcome to the game
    print("\n Let's play Word Games!\n-----------------------\n",
          "You enter a sentence. The program translates your sentence to\n",
          "Pig Latin and Turkey Irish plus prints a count of the vowels in\n",
          "your sentence. Please enter a sentence of at least three words:")
    # Loop through game cycle
    while (gameCount < MAX_GAMES):
        
        try:
            # Get player's string
            targetList = getString()
            
            # Print player's string in pigLatin
            pigLatin( targetList )
            
            # Print player's string in turkeyIrish
            turkeyIrish( targetList )
            
            # Print number of vowels in player's string
            countVowels( targetList )
            
            # Add 1 to gameCount
            gameCount = gameCount + 1

        except Exception as err:
            # Print any error message
            print("\n- - - ERROR - - -:\n\n",err,'\n\n- - - - - - - - -\n\n')

# Get player's string and validate that it has a minimum of 3 words
def getString():

    newString = input("\nPlease enter your sentence:\n>   ")
    # Strip beginning and trailing spaces
    newString = newString.strip() 

    # Validate string has a minimum of 3 words
    while not valid_sentence(newString):
        print("\nPlease enter something with three words or more.")
        newString = input("Enter your sentence:\n>   ")
    # Make sentence lowercase and into a list
    list_of_words = newString.lower().split()
    return(list_of_words)

# Validate string has a minimum of 3 words
def valid_sentence( stringofwords ):
    
    # Make sentence into a list
    word_list = stringofwords.lower().split()

    # Set boolean variables to False
    correct_number_of_words = False

    # Find length of word_list and verify it is longer than 2, return true
    if len(word_list) > 2:
        correct_number_of_words = True
        
    # If list has correct number of words return True otherwise return False
    if correct_number_of_words:
        is_valid = True
    else:
        is_valid = False
        
    #return validation
    return is_valid
        
def pigLatin( word_list ):

    # Initialize empty string
    pig_lat_sentence = ""

    # Loop through pig_lat_sentence list
    for word in word_list:
        first_letter = word[:1]
        rest_of_word = word[1:]
        new_word = rest_of_word + first_letter + "ay "
        pig_lat_sentence = pig_lat_sentence + new_word
        
    # Capitalizing Pig Latin sentence
    pig_lat_sentence = pig_lat_sentence[:1].upper()+pig_lat_sentence[1:] 
    # Print result
    print("\nYour sentence in Pig Latin:",pig_lat_sentence)

def turkeyIrish( word_list ):
    # Initialize empty string
    sentence = ""

    # Loop over word_list
    for word in word_list:

        # Make list into sentence
        sentence = sentence + word + " "
        
    # Make sentence lowercase 
    sentence = sentence.lower()
    
    # Initialize list of vowels
    list_of_vowels = ["a","e","i","o","u"]
    
    # Initialize empty string
    tur_irish_sentence = ""

    # Loop over sentence
    for ch in sentence:
        # If in list_of_vowels add ab
        if ch in list_of_vowels:
            tur_irish_sentence = tur_irish_sentence + "ab" + ch
        # If not in list_of_vowels return ch
        else:
            tur_irish_sentence = tur_irish_sentence + ch
    # Capitalizing Turkey Irish sentence
    tur_irish_sentence = tur_irish_sentence[:1].upper()+tur_irish_sentence[1:]
    # Print result
    print("\nYour sentence in Turkey Irish:",tur_irish_sentence)

def countVowels( word_list ):
    # Initialize empty string
    sentence = ""

    # Loop over word_list
    for word in word_list:

        # Make list into sentence
        sentence = sentence + word

    # Make sentence lowercase
    sentence = sentence.lower()
    # Initialize counter number_of_vowels to 0
    number_of_vowels = 0
    # Look for vowels in sentence
    for vowel in sentence:
        if vowel == "a":
            number_of_vowels += 1
        if vowel == "e":
            number_of_vowels += 1
        if vowel == "i":
            number_of_vowels += 1
        if vowel == "o":
            number_of_vowels += 1
        if vowel == "u":
            number_of_vowels += 1
        
    print("\nYour sentence contained:", number_of_vowels,"vowel(s)")

main()

# Outro: say thank you and goodbye
print("\n\nThank you for playing Word Games.")
print("Hope you found it interesting and had fun!\n\n")


'''
------
OUTPUT
------
>>> 
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_7.py ======

 Let's play Word Games!
-----------------------
 You enter a sentence. The program translates your sentence to
 Pig Latin and Turkey Irish plus prints a count of the vowels in
 your sentence. Please enter a sentence of at least three words:

Please enter your sentence:
>   Are you feeling lucky punk

Your sentence in Pig Latin: Reaay ouyay eelingfay uckylay unkpay 

Your sentence in Turkey Irish: Abarabe yaboabu fabeabelabing labucky pabunk 

Your sentence contained: 9 vowel(s)

Please enter your sentence:
>   Are you looking at me

Your sentence in Pig Latin: Reaay ouyay ookinglay taay emay 

Your sentence in Turkey Irish: Abarabe yaboabu laboabokabing abat mabe 

Your sentence contained: 9 vowel(s)

Please enter your sentence:
>   sos

Please enter something with three words or more.
Enter your sentence:
>   s o s

Your sentence in Pig Latin: Say oay say 

Your sentence in Turkey Irish: S abo s 

Your sentence contained: 1 vowel(s)


Thank you for playing Word Games.
Hope you found it interesting and had fun!


>>> 
'''
 
