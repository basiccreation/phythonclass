      
class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correctanswer):
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
        return "Question: " + self.__question

# The programs main functions
def main():
    try:
        # phones = make_list()
        list_of_questions = createQuestionsAnswers()
        # display_list(phones)
        display_list(list_of_questions)
        
    except Exception as err:
        print("\n--------------------------------")
        print("Oops, there's an error in main()")
        print("It says,",err,'\n\n')
     
def createQuestionsAnswers():
    # Create an empty list.
    # phone_list = []
    question_object_list = []


    # questionlist = [
    
    list_of_questions_options_and_answer = [
        ["Which of these scientists was the first to theorize quantized energy?",
          "Albert Einstein",
          "Werner Heisenberg",
          "Edward Schrodinger",
          "Max Planck",
          4],
         ["Most of the advancements in quantum physics arose from physicists trying to understand the nature of this very common form of energy. Which form of energy was postulated to have a dual nature, comprising of waves and particles?",
          "Light",
          "Wind",
          "Wave",
          "Sun",
          1],
         ["Which is the name given to one of the fundamental principles of quantum physics?",
          "Biparticle Policy",
          "The Mixed Double of Quantum Mechanics",
          "Twin Particle Constellation",
          "Wave Particle Duality",
          4],
         ["Space outside of our regular third dimension is known as what type of space?",
          "",
          "Euclidean",
          "",
          "",  
          2],
         ["A fourth dimension hypercube is known as a what?",
          "a",
          "Tesseract",
          "c",
          "d",
          2],
         ["Who said: 'Anyone who is not shocked by quantum theory, has not understood it'?",
          "Niels Bohr",
          "Albert Einstein",
          "Nikolas Tesla",
          "d",
          1],
         ["The word 'astrophysics' is based on Greek words. Do you know which of these bodies 'astro' translates to?",
          "Sun",
          "Moon",
          "Star",
          "Planet",
          3],
         ["Scientists who study astrophysics might also learn about the chemical composi",
          "Mars",
          "Jupiter",
          "Venus",
          "Mercury",
          2],
         ["Astrophysicists sometimes study about the temperature of stars. Which of these stars would be the hottest?",
          "Yellow star",
          "White star",
          "Red star",
          "Blue star",
          4],
         ["Astrophysicists sometimes study galaxies. The word 'galaxy' comes from the Greek, a word meaning what?",
          "Spiral",
          "Universe",
          "Starry",
          "Milky",
          4]
         ]
    
        
        # Loop through list_of_questions_options_and_answer
    for item in list_of_questions_options_and_answer:  

        # Get the information
        question = item[0]
        option1 = item[1]
        option2 = item[2]
        option3 = item[3]
        option4 = item[4]
        answer = item[5]

        # Create a new Question object in memory and
        # Assign it to the trivia_question variable.
        trivia_question = Question(question, option1, option2, option3, option4, answer)
        question_object_list.append(trivia_question)

    return question_object_list

def display_list(question_object_list):
    for item in question_object_list:
        print(item.get_question())
        print(item.get_answer1())
        print(item.get_answer2())
        print(item.get_answer3())
        print(item.get_answer4())
        print(item.get_correctanswer())
        print()
        
main()
'''
------
OUTPUT
------


'''
