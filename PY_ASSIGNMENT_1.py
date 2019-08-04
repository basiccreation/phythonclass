# Hello World! program.
# main accepts user input and prints a greeting using the input plus
# prints header and bullets from section 6 in syllabus

def main():
    
    # Header and bullets from section 6 in syllabus
    S6_header = "S.6 Where Everything Happens"
    S6_bullet1 = "• Assignments: submitted through the Assignments."
    S6_bullet2 = "• Tests: taken through the Quizzes"
    S6_bullet3 = "• Questions or comments: posted using the Discussions"

    # Get the user's name
    name = input('What is your name? ')

    # Print greeting
    print("Hello World! I am", name)

    # Print header and bullets from section 6 in syllabus
    print(S6_header)
    print(S6_bullet1)
    print(S6_bullet2)
    print(S6_bullet3)

# Call the main function
main()

"""
#--------- OUTPUT -----------
================== RESTART: /Users/piasmith/Desktop/test.py ==================
What is your name? 007
Hello World! I am 007
S.6 Where Everything Happens
• Assignments: submitted through the Assignments.
• Tests: taken through the Quizzes
• Questions or comments: posted using the Discussions
>>> 
================== RESTART: /Users/piasmith/Desktop/test.py ==================
What is your name? pia
Hello World! I am pia
S.6 Where Everything Happens
• Assignments: submitted through the Assignments.
• Tests: taken through the Quizzes
• Questions or comments: posted using the Discussions
>>> 
================== RESTART: /Users/piasmith/Desktop/test.py ==================
What is your name? 
Hello World! I am 
S.6 Where Everything Happens
• Assignments: submitted through the Assignments.
• Tests: taken through the Quizzes
• Questions or comments: posted using the Discussions
#----------------------------
"""
