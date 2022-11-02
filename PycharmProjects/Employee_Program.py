# Program to calculate and display gross pay for some employees

# Named constant that indicates the number of employees
NUM_EMPLOYEE = 6
# Variable to hold the pay rate
pay_rate = 8
# List to hold hours worked by each employee
hours_worked = [0] * NUM_EMPLOYEE

# loop to collect hours worked
# Enter number hours worked for employee X:
def getInput():
    for index in range(NUM_EMPLOYEE):
        print('Enter number of hours worked for employee: ', index + 1, ': ', sep='', end='')
        hours_worked[index] = float(input())

# Get the hourly rate
pay_rate = float(input('Enter hourly rate: '))

def getDisplay():
# loop to display the gross pay
    for index in range(NUM_EMPLOYEE):
        gross_pay = hours_worked[index] * pay_rate
        print('Gross pay for employee', index + 1, ': £', format(gross_pay, '.2f'), sep='')

# Provide the total
    total = gross_pay * NUM_EMPLOYEE
    print('The overall total payment is', ': £', format(total, '.2f'), sep='')

# Call the functions
getInput()

getDisplay()