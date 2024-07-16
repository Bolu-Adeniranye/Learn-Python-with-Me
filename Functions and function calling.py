# # Define       (Parameters and default parameter)
# def greeting(name,age="28"):
#     # print("Hello " + name + ", you are " + age + "!")
#     print(f"Hello {name}, you are {age}!")

# name = input("Enter your name: ") 
# # Arguments
# greeting(name,"32")
# greeting("Judith")



def greeting(name, age=28, color="red"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print(f'Hello {name.capitalize()}, you are will be {age + 1} next year!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input("What color do you like: ")
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 


greeting(name, int(age), color)