#!/usr/bin/env python 3.7

#getting user input

name = input("what is your name? ")
color = input("What is your favorite color: ")
age = int(input("How old are you today?: "))



#instead of default /n - end with a space 
#print(name, end=" ")
#print("is " + str(age) + " years old", end=" ")
#print("With a favorite color of " + color + ".")


#print this "list" and seperate with a space 
print(name, 'is', age, 'years old and loves the color', color + '.' , sep =" ")
# sep is deffault to a space 
#print(name, 'is', age, 'years old and loves the color', color + '.')

