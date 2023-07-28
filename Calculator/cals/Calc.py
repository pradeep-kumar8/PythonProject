print("Welcome to calculator Created by 'Pradeep'")
# First of all provde user to Choice Hint
print("Addition = 1")
print("Subtraction = 2")
print("Multiplication = 3")
print("Division = 4")
print("Exit = 5")

#We need to import all function from caltask to perform all task
# from caltask import add, minus, multiply, division
from caltask import *


# we use infinity loop till user not exit can perform multiple task
while True:
    # User choice input
    user_input = input("\nSelect your Choice 1-5 -: ")

    # if user give wrong value or other input it'll be raise error so handling this error use try except
    try:
        if int(user_input) == 1:
            print("----Addition----")
            Num1 = int(input("First Number : "))
            Num2 = int(input("Second Number : "))
            add(Num1, Num2)
        elif int(user_input) == 2:
            print("----Subtraction----")
            Num1 = int(input("First Number : "))
            Num2 = int(input("Second Number : "))
            minus(Num1, Num2)
        elif int(user_input) == 3:
            print('----Multiplication----')
            Num1 = int(input("First Number : "))
            Num2 = int(input("Second Number : "))
            multiply(Num1, Num2)
        elif int(user_input) == 4:
            print('----Division----')
            Num1 = int(input("First Number : "))
            Num2 = int(input("Second Number : "))
            # if user input is 0 that can infinity so we will show user msg for infinity
            if Num2 == 0:
                print("You can't devide by 0")
            else:
                division(Num1, Num2)
        elif int(user_input) == 5:
            print("Your are exit now")
            break
        else:
            print("Invalid Input")
    except ValueError:
        print("Value Error")
