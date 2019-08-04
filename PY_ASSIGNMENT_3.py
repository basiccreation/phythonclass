"""
Pia Smith
------------------------
The Candy Locker Program
------------------------
main() accepts user input and simulates that
the user's candy bar locker will be stocked with
15 candy bars at the beginning of each month.

During the month the user can 'consume', 'replenish'
or 'lose' candy bars depending of the choices made
by the user.

Any bars that are not consumed at the end of the
month are lost and the locker will be restocked
with a new batch of 15.
"""
def main():
    # Global variables
    keep_going = "y" #boolean variable y/n
    menu_item = 0 #menu item
    consume = 0 #number of bars user wants to consume
    current_bar_total = 15 #user's current bar total
    current_tab_total = 15 #user's current tab total
    divider = "------------------------------------" #divider for readability
    
    # Intro message - shown once
    print("\n\nInitial Account")
    print(divider)
    print("Locker: Available number of candy bars:",current_bar_total)
    print("Tab: Amount owed at this time: $",current_tab_total)

    # Show selection menu
    while keep_going == "y":
        for menu_item in ["\nMenu",
                          "1. Current Bill and Start New Month",
                          "2. Total Number of Bars Available",
                          "3. Consume Bars",
                          "4. Buy More Bars",
                          "5. Final Bill"]:
            print(menu_item)

        # Get menu user selection
        select_menu_item = ("\nHi! Make your selection from the menu.  ")
        try_again = ("\nPlease try again. Select a number between 1 and 5. ")
        user_selection = int(input(select_menu_item))

        # Check user selects a number between 1-5
        while user_selection < 0 or user_selection > 5:
            user_selection = int(input(try_again))

        """Print output simulating
        - getting the monthly bill and finalize account for month",
        - showing current locker content
        - consuming bars
        - buying more bars
        - showing current bill and closing program
        """
        if (user_selection == 1):
            # Show current selection
            current_menu_selection = 1
            print("\nYou selected number:", current_menu_selection)
            print(divider)
            print("Current Bill and Start New Month")
            print(divider)
            # Show current locker content
            print("Unused bars (lost): \t",current_bar_total)
            # Show current bill
            print("Final amount due now: \t", current_tab_total)
            # Reset to 15 bars and show current locker content
            print("\nStarting New Month")
            current_bar_total = 15
            print("Bars in locker:\t",current_bar_total)
            print(divider)
            # Show menu again so user can make another choice
            keep_going = "y"
            
        elif (user_selection == 2):
            # Show current selection
            current_menu_selection = 2
            print("\nYou selected number:", current_menu_selection)
            print(divider)
            print("Total Number of Bars Available")
            print(divider)
            # Show current content in locker
            print("Bars in locker:\t",current_bar_total)
            print(divider)
            # Show menu again so user can make another choice
            keep_going = "y"
        elif (user_selection == 3):
            # Show current selection
            current_menu_selection = 3
            print("\nYou selected number:", current_menu_selection)
            print(divider)
            print("Consume Bars")
            print(divider)
            # Get user input
            consume = int(input("\nHow many would you like to consume?   "))
            # Check user entered number within accepted range
            while consume < 0 or consume > 10:
                print("You can only consume 10 bars at a time. Please")
                consume = int(input("enter a new number.   "))
            # Check if user locer has enough bars, alert user if they don't
            # and add 10 bars to locker and charge their account
            if(consume > current_bar_total):
                print("\nALERT!!")
                print("Not enough bars in your locker.")
                print("\nAutomatic replenishment")
                print("Added to locker:\t10")
                current_bar_total = current_bar_total + 10
                print("Added to tab:\t15")
                current_tab_total = current_tab_total + 15
            # If locker has enough bars, deduct bars from locker total
            current_bar_total = current_bar_total - consume
            
            # Show current locker tototal
            print("\nBars in locker:\t",current_bar_total)
            print(divider)
            # Show menu again so user can make another choice
            keep_going = "y"
        elif (user_selection == 4):
            # Show current selection
            current_menu_selection = 4
            print("\nYou selected number:", current_menu_selection)
            print(divider)
            print("Buy More Bars")
            print(divider)
            # Show user purchase options
            for purchase_option in ["\nHow many would you like to buy?",
                                    "1. 10 more bars",
                                    "2. 20 more bars",
                                    "3. 30 more bars"]:
                print(purchase_option)
                
            # Get user input
            purchase = int(input("\nSelect a number between 1 and 3.  "))

            # Check user selected a number between 1-3 
            while (purchase < 0 or purchase > 3):
                print("\nThat is not an option. Please")
                purchase = int(input("select a number between 1 and 3.   "))
            # Add the relevant amount to bars to locker and
            # charge the corresponding amount to the account
            if(purchase == 1):
                print("\nAdded to locker:\t10")
                current_bar_total = current_bar_total + 10
                print("Added to tab:\t11")
                current_tab_total = current_tab_total + 11
            elif(purchase == 2):
                print("\nAdded to locker:\t20")
                current_bar_total = current_bar_total + 20
                print("Added to tab:\t22")
                current_tab_total = current_tab_total + 22
            elif(purchase == 3):
                print("\nAdded to locker:\t30")
                current_bar_total = current_bar_total + 30
                print("Added to tab:\t33")
                current_tab_total = current_tab_total + 33
            print("\nBars in locker:\t",current_bar_total)
            print(divider)
            # Show menu again so user can make another choice
            keep_going = "y"

        elif (user_selection == 5):
            # Show current selection
            current_menu_selection = 5
            print("\nYou selected number:", current_menu_selection)
            print(divider)
            print("Final Bill")
            print(divider)
            # Show final bill and close program
            print("Final amount due now: \t", current_tab_total)
            print("\nThank you,\nYour Friends at Candy Bar Locker")
            print(divider)
            # Close the program
            keep_going = "n"

main()

"""
--------- OUTPUT -----------

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: /Users/piasmith/Desktop/PYTHON class/PY_ASSIGNMENT_3.py ======


Initial Account
------------------------------------
Locker: Available number of candy bars: 15
Tab: Amount owed at this time: $ 15

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  3

You selected number: 3
------------------------------------
Consume Bars
------------------------------------

How many would you like to consume?   10

Bars in locker:	 5
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  2

You selected number: 2
------------------------------------
Total Number of Bars Available
------------------------------------
Bars in locker:	 5
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  3

You selected number: 3
------------------------------------
Consume Bars
------------------------------------

How many would you like to consume?   9

ALERT!!
Not enough bars in your locker.

Automatic replenishment
Added to locker:	10
Added to tab:	15

Bars in locker:	 6
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  1

You selected number: 1
------------------------------------
Current Bill and Start New Month
------------------------------------
Unused bars (lost): 	 6
Final amount due now: 	 30

Starting New Month
Bars in locker:	 15
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  4

You selected number: 4
------------------------------------
Buy More Bars
------------------------------------

How many would you like to buy?
1. 10 more bars
2. 20 more bars
3. 30 more bars

Select a number between 1 and 3.  5

That is not an option. Please
select a number between 1 and 3.   2

Added to locker:	20
Added to tab:	22

Bars in locker:	 35
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  8

Please try again. Select a number between 1 and 5. 2

You selected number: 2
------------------------------------
Total Number of Bars Available
------------------------------------
Bars in locker:	 35
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  1

You selected number: 1
------------------------------------
Current Bill and Start New Month
------------------------------------
Unused bars (lost): 	 35
Final amount due now: 	 52

Starting New Month
Bars in locker:	 15
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  4

You selected number: 4
------------------------------------
Buy More Bars
------------------------------------

How many would you like to buy?
1. 10 more bars
2. 20 more bars
3. 30 more bars

Select a number between 1 and 3.  1

Added to locker:	10
Added to tab:	11

Bars in locker:	 25
------------------------------------

Menu
1. Current Bill and Start New Month
2. Total Number of Bars Available
3. Consume Bars
4. Buy More Bars
5. Final Bill

Hi! Make your selection from the menu.  5

You selected number: 5
------------------------------------
Final Bill
------------------------------------
Final amount due now: 	 63

Thank you,
Your Friends at Candy Bar Locker
------------------------------------
>>> 

----------------------------
"""
