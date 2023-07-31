import math

# Simple Function to perform the calculation
def calculate(num1, num2, operator):
    result = 0
    if operator == '+':
        result = round(num1 + num2)
    elif operator == '-':
        result = round(num1 - num2)
    elif operator == '*':
        result = round(num1 * num2)
    elif operator == '/':
        result = round(num1 / num2)
    elif operator == '^':
        result = round(math.pow(num1, num2))
    elif operator == 'sqrt':
        result = round(math.sqrt(num1))
    else:
        print("Invalid operator!")
        return None # By default the result will always return not None
        
    return result

    

# Simple Python Calculator with Functions

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        operator = input("Enter an operator (+, -, *, /, ^, sqrt): ")
       
        # Call and invoke function
        result = calculate(num1, num2, operator)

        # Print result if the calculation successful
        # The result always print in loop as long the result is 0.
        # Note that 0 is used as the default return value instead of None,
        # so that the main program can distinguish between a successful
        # calculation that results in 0, and a calculation that fails due to an invalid operator.
        if result is not None:
            print("The result of {num1} {operator} {num2} is: {result}".
            format(num1=num1, operator=operator, num2=num2, result=result))
        
    # Handling error    
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    # Ask user to calculate again or not
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice != 'y':
        break