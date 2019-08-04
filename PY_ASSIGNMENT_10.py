'''
Pia Smith
CS F021A PYTHON FOR PROGRAMMERS (Su19)
--------------------------------------
Assignment 10
Employee class and subclass

The Program Spec:

User enters employee data programs prints it to screen for verification.

Create a run and include it as output with your program.
Be sure to show that the validation works for the possible answers.

'''

# Employee class
class Employee:
    # The __init__ method accepts arguments for
    # Employee name and Employee number.

    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # set mutators
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # Set accessors
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

        def __str__(self):
            return "returning from employee"

# Production Worker class
class ProductionWorker(Employee):

    # The __init__ method accepts arguments for employee name, 
    # number, shift number and hourly pay rate

    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):

        # Call Employee superclass
        Employee.__init__(self, employee_name, employee_number)

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
        
def main():

    print("Enter Employee information below:")

    ''' Get worker data'''
    # Get Name
    name = input("Name: ")

    # Verify name is at least two entries long
    while len(name.strip().split()) < 2:
        name = input("Enter full name: ")

    # Get employee number
    number = int(input("Number: "))

    # Verify employee number is 3 digits
    while number < 100 or number > 999:
        number = int(input("Employee number is 3 digits: "))    

    # Get shift
    shift = int(input("Shift: "))

    # Verify it is either 1 or 2
    while shift < 0 or shift > 2:
        shift = int(input("Enter 1 for Day and 2 for Night: "))

    # Get pay rate
    rate = float(input("Rate: "))

    # Verify the amount is correct
    while rate not in [20.00,30.00,40.00]:
        print("Check the rate again. Should be either:")
        rate = float(input("Regular hours: $20, plus 50%: $30 or double: $40"))

    # Create object from ProductionWorker class
    worker_entry = ProductionWorker(name, number, shift, rate)
        
    # Display the entered data
    print("\n\nYou entered:\n------------")
    print("Employee Name:", worker_entry.get_employee_name())
    print("Employee Number:", worker_entry.get_employee_number())
    print("Work Shift:", worker_entry.get_shift_number(),"-", worker_entry.shift_description())
    print("Pay Rate: $", format(worker_entry.get_hourly_pay_rate(), ',.2f'), sep='')
    print("------------------")
    print(worker_entry)

main()
'''
-------
OUTPUT
-------

'''
