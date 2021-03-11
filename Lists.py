#!/usr/bin/env python 3.7
#Lists

my_list = [1,2,3,4,5]
other_list = ['a',1,1.2,True]
# Lists can hold type of variables

#indexes the same as strings
# my_list[0] = returns 1
# step works same
# list is always return instead of string

# Lists are Mutable
my_list[0]='z'

# adding 
# my_list + [8,9,10]
# making new list 
my_list += [8,9,10]

# assinging new list to a slice
my_list[1:3] = ['b','c'] # = ['b','c','d','e'] # can increase size too 

# deletion 
my_list[4:]= [] # after 4 nothing else
# or 

del my_list[0] 
