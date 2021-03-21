#!/usr/bin/env/python 3.7


# start with def, snake case, (parameters)
# def function_name(Parameters)

#function_names(arugments)
 
def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

#positional argument call
contact_card("keith", 29, "Honda Civic")

#keyword arguments
contact_card(age=29, car_model="Honda Civic", name="keith")
#or mix...  but must continue keyword once used.
contact_card("keith", age=29, car_model="Honda Civic")

#key word useful with default parameters
def can_drive(age, driving_age=16)
# default paramenters cannot be followed by non default 
# driving_age = 16, type=,.... 


#Recursion- calling a function from within itself
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))

print(fib(item_to_calculate))