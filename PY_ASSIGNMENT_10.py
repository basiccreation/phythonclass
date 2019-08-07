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
        
        # Initialize __employee_name attribute
        # self.__employee_name = employee_name

        # Initialize __employee_number attribute
        # self.__employee_number = employee_number

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

    # Set __set__
    def __str__(self):
        return "\n\nYou entered:\n------------------" +\
               "\nEmployee Name: " + str(self._employee_name) +\
               "\nEmployee Number: " + str(self._employee_number) +\
               "\nWork Shift: " + str(self.__shift_number) + " - " + \
               self.shift_description() +\
               "\nPay Rate $: " +\
               format(self.__hourly_pay_rate, ',.2f') +\
               "\n------------------"
    
# main() contains programs main     
def main():

    # Ask for user input
    print("Enter Employee information below:")

    ''' Get Worker Data'''
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

    # Verify the amount is either regular pay, plus 50% or double
    while rate not in [20.20,30.30,40.40]:
        #print("Check the rate again.\n- Regular hours: $20.20")
        #print("- Plus 50%: $30.30\n- double: $40.40")
        print("Check the rate again.")
        print("- Regular:  $20.20")
        print("- Plus 50%: $30.30")
        print("- Double:   $40.40")
        rate = float(input("> "))

    # Create object from ProductionWorker class
    worker_entry = ProductionWorker(name, number, shift, rate)
    '''   
    # Display the entered data
    print("\n\nYou entered:\n------------------")
    
    print("Employee Name:",
          worker_entry.get_employee_name())
    
    print("Employee Number:",
          worker_entry.get_employee_number())
    
    print("Work Shift:",
          worker_entry.get_shift_number(),"-",
          worker_entry.shift_description())
    
    print("Pay Rate: $",
          format(worker_entry.get_hourly_pay_rate(), ',.2f'), sep='')
    
    print("------------------")
    '''
    print(worker_entry)
    

main()
'''
-------
OUTPUT
-------

'''
