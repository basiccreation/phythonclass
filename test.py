        
        '''
        #Get user input
        select_menu_item = ("\nWhat would you like to do? Select a number between 1-5 ")
        try_again = ("Please try again. Select a number between 1 and 5")
        user_selection = int(input(select_menu_item))

        #Check user selected a number between 1-5
        while user_selection < 0 or user_selection > 5:
            user_selection = int(input(try_again))

        #Print selection
        if (user_selection == 1):
            current_menu_selection = 1
            print("You selected", current_menu_selection)
            keep_going = "y"
        elif (user_selection == 2):
            current_menu_selection = 2
        elif (user_selection == 3):
            current_menu_selection = 3   
        elif (user_selection == 4):
            current_menu_selection = 4        
        elif (user_selection == 5):
            current_menu_selection = 5

    
        '''

        for 

#Get user input
    select_menu_item = ("\nWhat would you like to do? Select a number between 1-5 ")
    try_again = ("Please try again. Select a number between 1 and 5")
    user_selection = int(input(select_menu_item))

    #Check user selected a number between 1-5
    while user_selection < 0 or user_selection > 5:
        user_selection = int(input(try_again))

#Print selection
    if (user_selection == 1):
        current_menu_selection = 1
        print("You selected", current_menu_selection)
    elif (user_selection == 2):
        current_menu_selection = 2
    elif (user_selection == 3):
        current_menu_selection = 3   
    elif (user_selection == 4):
        current_menu_selection = 4        
    elif (user_selection == 5):
        current_menu_selection = 5





