'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 9
Trivia Game

The Program Spec:

    Each player will take turn answering a total of
    10 questions. 5 for each player.  If the player
    selects the correct answer, they earn a point.    
    At the end, a winner is declared.

    -------------------------------------------------
    
     
    Create a run and include it as output with your program.
    Be sure to show that the validation works for the
    possible answers.

'''
  
class Question:
    def __init__(self, question, answer1, answer2, answer3,
                 answer4, correctanswer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctanswer = correctanswer

    def set_question(self, question):
        self.__question = question
        
    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_correctanswer(self, correctanswer):
        self.__correctanswer = correctanswer

    def get_question(self):
        return self.__question
        
    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4
    
    def get_correctanswer(self):
        return self.__correctanswer

    def __str__(self):
        return "Your Question Is: \n\n" + self.__question +\
               "\n\n1. " + self.__answer1 +\
               "\n2. " + self.__answer2 +\
               "\n3. " + self.__answer3 +\
               "\n4. " + self.__answer4 +\
               "\n"

# The programs main functions
def main():
    try:
        # Pull in list of question objects
        list_of_questions = createQuestionsAnswers()

        # Initialize counter
        game_counter = 1
        
        # Initialize totals
        player_one_total = 0
        player_two_total = 0

        # Initialize player variables
        player_one_name = "Player One"
        player_two_name = "Player Two"

        # Get the players' names
        player_one_name = input("\nPlayer One, what's your name?\n>  ")
        player_two_name = input("\nPlayer Two, what's your name?\n>  ")

        for item in list_of_questions:

            # Loop through Player One's games
            if game_counter in [1,3,5,7,9]:

                # Greet Player One
                print("--------------------------------\n\n")
                print("It's your turn",player_one_name,"\n")

                # Print question and multiple choice
                print(item)
                
                # Get player One's guess
                player1 = int(input(">   "))

                # Validate input is between 1 and 4
                while player1 < 0 or player1 > 4:
                    print("\nOops! There are only four possible answers.")
                    player1 = int(input("Please enter: 1, 2, 3 or 4\n>   "))


                # Player One is told whether they got it right or not.
                if player1 == item.get_correctanswer():
                    print(player1, "is correct, you earned 1 point.")
                    player_one_total += 1
                else:
                    print(player1,"is wrong, you get 0 points.")
                    
            # Loop through Player Two's games
            if game_counter in [2,4,6,8,10]:

                # Greet Player Two
                print("--------------------------------\n\n")
                print("It's your turn", player_two_name,"\n")

                # Print question and multiple choice
                print(item)
                
                # Get player Two's guess
                player2 = int(input(">   "))

                # Validate input is between 1 and 4
                while player2 < 0 or player2 > 4:
                    print("\nOops! There are only four possible answers.")
                    player2 = int(input("Please enter: 1, 2, 3 or 4\n>   "))

                # Player Two is told whether they got it right or not.
                if player2 == item.get_correctanswer():
                    print(player2, "is correct, you earned 1 point.")
                    player_two_total += 1
                else:
                    print(player2,"is wrong, you get 0 points")

            # Add one to counter so it alternates between players
            game_counter += 1

        # Announce end of game
        print("\n-------------------------------------------")
        print("That's the end of the game. Final score is:")

        # Announce points earned to players
        print(player_one_name, "has",
              player_one_total,"points and",
              player_two_name, "has",
              player_two_total,"points.\n")
        
        # Announce the winner
        if player_one_total > player_two_total:
              print(player_one_name, "won, well done!!")
        elif player_one_total < player_two_total:
              print(player_two_name, "won, well done!!")
        else:
              print("It was a tie, well done both of you!!")

    except Exception as err:
        print("\n--------------------------------")
        print("Oops, there's an error in main()")
        print("It says,",err,'\n\n')

# createQuestionsAnswers() creates a list of Question objects
def createQuestionsAnswers():
    try:
        question_object_list = []

        # List that contains 10 question objects
        list_of_questions_options_and_answer = [
        [''.join(["Which of these scientists was the first to \n",
                  "theorize quantized energy?"]),
          "Albert Einstein",
          "Werner Heisenberg",
          "Edward Schrodinger",
          "Max Planck",
          4],
         [''.join(["Most of the advancements in quantum physics\n",
                  "arose from physicists trying to understand the\n",
                  "nature of this very common form of energy. Which\n",
                  "form of energy was postulated to have a dual\n",
                  "nature, comprising of waves and particles?"]),
          "Light",
          "Wind",
          "Wave",
          "Sun",
          1],
         [''.join(["Which is the name given to one of the \n",
                  "fundamental principles of quantum physics?"]),
          "Biparticle Policy",
          "The Mixed Double of Quantum Mechanics",
          "Twin Particle Constellation",
          "Wave Particle Duality",
          4],
         [''.join(["Space outside of our regular third \n",
                  "dimension is known as what type of space?"]),
          "Geospace",
          "Euclidean",
          "Baryonic",
          "Magnetosphere",  
          2],
         ["A fourth dimension hypercube is known as a what?",
          "Rubics",
          "Tesseract",
          "Limaçon",
          "Twisted cubic",
          2],
         [''.join(["Who said: 'Anyone who is not shocked \n",
                  "by quantum theory, has not understood it'?"]),
          "Niels Bohr",
          "Albert Einstein",
          "Nikola Tesla",
          "Richard Feynman",
          1],
         [''.join(["The word 'astrophysics' is based on Greek \n",
                  "words. Do you know which of these bodies \n",
                  "'astro' translates to?"]),
          "Sun",
          "Moon",
          "Star",
          "Planet",
          3],
         [''.join(["Scientists who study astrophysics \n",
                  "might also learn about the chemical \n",
                  "composition of planets. Which of these \n",
                  "planets could you not stand on because \n",
                  "it is mostly gas?"]),
          "Mars",
          "Jupiter",
          "Venus",
          "Mercury",
          2],
         [''.join(["Astrophysicists sometimes study \n",
                  "about the temperature of stars. Which of\n",
                  "these stars would be the hottest?"]),
          "Yellow star",
          "White star",
          "Red star",
          "Blue star",
          4],
         [''.join(["Astrophysicists sometimes study galaxies.\n",
                  "The word 'galaxy' comes from the Greek,\n",
                  "a word meaning what?"]),
          "Spiral",
          "Universe",
          "Starry",
          "Milky",
          4]
         ]
    
        # Loop through list_of_questions_options_and_answer
        for item in list_of_questions_options_and_answer:  

            # Get the information and assign to variables
            question = item[0]
            option1 = item[1]
            option2 = item[2]
            option3 = item[3]
            option4 = item[4]
            answer = item[5]

            # Create a new Question object in memory and
            # Assign to the trivia_question variable.
            trivia_question = Question(question, option1, option2,
                                       option3, option4, answer)

            # Append to question_object_list 
            question_object_list.append(trivia_question)

        # Return question_object_list list
        return question_object_list

    except Exception as err:
        print("\n--------------------------------")
        print("Oops, there's an error in createQuestionsAnswers()")
        print("It says,",err,'\n\n')
        
main()
'''
------
OUTPUT
------


'''
