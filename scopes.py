#!/usr/bin/env/python 3.7

if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x += 1

print(x)

# conditionals and loops do not change/have their own scope. 
# print has access to while x, while has access to if x

# functions/classes change scope 

def set_y():
    y=5

set_y()

# print(y)
# print y will not work
#

z = 5

def set_x(z):
    print("Inner z:", z)
    x = z
    z = x

set_x(10)
print("Outer z :", z)

# first print is 10 second is 5
# using doin this is called name hiding or shadowing ,
#  higher level gets hidden when z is passed 10


