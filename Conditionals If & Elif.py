is_raining = True
is_cold = True
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Umbrella is optional")


# amount = 50
# if amount <= 50:
#     print("Purchase approved")
# else:
#     print("Please enter your pin!")

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
# num1 = float(input('Enter first number: '))
# if mode.lower() == 'f':
#     print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
# else:
#     num2 = float(input('Enter second number: '))

#     if mode == '+':
#         print(f'Answer is: {num1 + num2}')
#     elif mode == '-':
#         print(f'Answer is: {num1 - num2}')
#     elif mode == '*':
#         print(f'Answer is: {num1 * num2}')
#     elif mode == '/':
#         print(f'Answer is: {num1 / num2}')
#     else:
#         print('Input error!')


# Conditionals Exercise

def num_days(month):

    # if month == 'jan':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'apr':
    #     print('number of days in',month,'is',30)
    # elif month == 'may':
    #     print('number of days in',month,'is',31)
    # elif month == 'jun':
    #     print('number of days in',month,'is',30)
    # elif month == 'jul':
    #     print('number of days in',month,'is',31)
    # elif month == 'aug':
    #     print('number of days in',month,'is',31)
    # elif month == 'sep':
    #     print('number of days in',month,'is',30)
    # elif month == 'oct':
    #     print('number of days in',month,'is',31)
    # elif month == 'nov':
    #     print('number of days in',month,'is',30)
    # elif month == 'dec':
    #     print('number of days in',month,'is',31)
        
        
    if month == 'jan' or 'mar' or 'may' or 'jul' or 'aug' or 'oct' or 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print('number of days in',month,'is',30)


        # OR


        days = 31
    if month in {'apr','jun','sep','nov'}:
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
    

num_days('mar')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
