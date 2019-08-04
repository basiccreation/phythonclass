

def main():
    #Global variables
    keep_going = "y"
    menu_item = 0
    current_bar_total = 15
    current_tab_total = 15
    divider = "-------------------------------------------"
    #Intro message
    print("\n\nInitial Account")
    print(divider)
    print("Available Number of Candy Bars:",current_bar_total)
    print("Amount owed at this time: $",current_tab_total)

    #Show Menu
    while keep_going == "y":
        for menu_item in ["\nMenu","1. Current Bill and Start New Month","2. Total Number of Bars Available","3. Consume Bars","4. Buy More Bars","5. Final Bill"]:
            print(menu_item)

        #Get user input
        select_menu_item = ("\nWhat would you like to do? Select a number between 1 and 5.  ")
        try_again = ("\nPlease try again. Select a number between 1 and 5. ")
        user_selection = int(input(select_menu_item))

        #Check user selected a number between 1-5
        while user_selection < 0 or user_selection > 5:
            user_selection = int(input(try_again))

        #Print selection
        if (user_selection == 1):
            current_menu_selection = 1
            print("\nYou selected", current_menu_selection)
            print(divider)
            print("Closing this Month's Bill")
            print(divider)
            print("Unused bars (lost): \t",current_bar_total)
            print("Final amount due now: \t", current_tab_total)
            print("\nStarting New Month")
            current_bar_total = 15
            print("New number of bars:\t",current_bar_total)
            print(divider)
            keep_going = "y"
            
        elif (user_selection == 2):
            current_menu_selection = 2
            print("\nYou selected", current_menu_selection)
            print(divider)
            print("Current Number of Candy Bars in your Locker")
            print(divider)
            print("Number of bars:\t",current_bar_total)
            print(divider)
            keep_going = "y"

main()
