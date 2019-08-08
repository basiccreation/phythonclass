'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 10
Employee class and subclass

The Program Spec:

User enters employee data. Programs prints it to screen for verification.

Create a run and include it as output with your program.
Be sure to show that the validation works for the possible answers.

'''

# Employee class
class Employee:
    
    # The __init__ method accepts arguments for
    # Employee name and Employee number.
    # ----------------------------------
    # Per Group Chat: Joshua Roche, changing dunder
    # to single underscores enables inheritance for
    # the sub-class
    def __init__(self, employee_name,
                 employee_number):
        self._employee_name = employee_name
        self._employee_number = employee_number

    # Set mutators
    def set_employee_name(self, employee_name):
        self._employee_name = employee_name

    def set_employee_number(self, employee_number):
        self._employee_number = employee_number

    # Set accessors
    def get_employee_name(self):
        return self._employee_name

    def get_employee_number(self):
        return self._employee_number

    # Set __str__
    def __str__(self):
        return "Employee name and number" +\
               "\n" + str(self._employee_name) +\
               "\n" + str(self._employee_number) +\
               "\n"   

# Production Worker Class
class ProductionWorker(Employee):

    # The __init__ method accepts arguments for employee name, 
    # number, shift number and hourly pay rate

    def __init__(self,
                 employee_name,
                 employee_number,
                 shift_number,
                 hourly_pay_rate):

        # Call Employee superclass
        Employee.__init__(self,
                          employee_name,
                          employee_number)

        # Initialize __shift_number attribute
        self.__shift_number = shift_number

        # Initialize __shift_number attribute
        self.__hourly_pay_rate = hourly_pay_rate

    # Set mutators
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
        
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # Set accessors
    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def shift_description(self):
        if self.__shift_number == 1:
            return "Day Shift"
        if self.__shift_number == 2:
            return "Night Shift"

    def formatted_rate(self):
        formatted = float(self.__hourly_pay_rate)
        formatted = "%.2f" % formatted 
        return formatted

    # Set __set__
    def __str__(self):
        return "\n\nYou entered:" +\
               "\n------------------" +\
               "\nEmployee Name: " + str(self._employee_name) +\
               "\nEmployee Number: " + str(self._employee_number) +\
               "\nWork Shift: " + str(self.__shift_number) + " - " +\
                                      self.shift_description() +\
               "\nPay Rate $: " + self.formatted_rate() +\
               "\n------------------"
    
# main() contains programs main     
def main():
    
    # Boolean variable y/n
    enter_another = "y" 

    # Keep entering another until user says no
    while enter_another == "y":

        # Ask for user input
        print("Enter Employee information below:")

        ''' Get Worker Data'''
        # Get Name
        name = input("Name: ")

        # Verify name is at least two entries long
        while len(name.strip().split()) < 2:
            name = input("Enter full name:\n> ")

        # Get employee number
        number = input("Number: ")
        
        # Verify number is a digit
        if number.isdigit():
            
            # Convert number to integer
            number = int(number)
            
            # Verify number is in range
            while int(number) < 100 or int(number) > 999:
                number = int(input("Employee number is 3 digits:\n> "))

        # Error message if number is alpha or alpha-numeric 
        elif number.isalpha() or number.isalnum():
            number = int(input("Employee number is 3 digits:\n> "))
            
            # Verify number is in range
            while int(number) < 100 or int(number) > 999:
                number = int(input("Employee number is 3 digits:\n> "))
                
        # Get shift
        shift = input("Shift: ")

        # If shift is a digit, change shift to an integer
        if shift.isdigit():
            shift = int(shift)

            # Verify it is either 1 or 2
            while shift < 0 or shift > 2:
                shift = int(input("Enter 1 for Day and 2 for Night:\n> "))

        # Error message if shift is alpha or alpha-numeric             
        elif shift.isalpha() or shift.isalnum():
            shift = int(input("Enter 1 for Day and 2 for Night:\n> "))
                        
        # Get pay rate
        rate = input("Rate: ")
        
        # if rate is a digit, change rate to a float
        if rate.isdigit():
            rate = float(rate)
            
            # Verify the amount is in range $20 - $30
            while rate < 20 or rate > 30:
                
                # Error message if rate is lower than 20 or higher than 40
                print("Check the rate again.")
                print("Rate should be between $20 and $40")
                rate = float(input("> "))
                
        # Error message if shift is alpha or alpha-numeric      
        elif rate.isalpha() or rate.isalnum():
            print("Check the rate again.")
            print("Rate should be between $20 and $40")
            rate = float(input("> "))
            
        # Create object from ProductionWorker class
        worker_entry = ProductionWorker(name, number, shift, rate)

        # Print the entered information
        print(worker_entry)

        # Ask user if they would like to enter another employee
        enter_another = input("Enter another? y/n\n> ")

main()
'''
-------
OUTPUT
-------
===== RESTART: /Users/piasmith/Desktop/python_class/PY_ASSIGNMENT_10.py =====
Enter Employee information below:
Name: Mads
Enter full name:
> Mads Mikkelsen
Number: 2
Employee number is 3 digits:
> 234
Shift: night
Enter 1 for Day and 2 for Night:
> 2
Rate: five
Check the rate again.
Rate should be between $20 and $40
> 23.45


You entered:
------------------
Employee Name: Mads Mikkelsen
Employee Number: 234
Work Shift: 2 - Night Shift
Pay Rate $: 23.45
------------------
Enter another? y/n
> n
>>>

'''
