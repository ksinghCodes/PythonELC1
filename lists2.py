#!/usr/bin/env python 3.7
#Lists

my_list=[1,2,3]

# add to with append method or +=
my_list.append(4)

#insert at a specific postion, adjust the rest
my_list.insert(0, 'a')

#postion of given object
my_list.index(3) 

#verify object is part of list

4 in my_list #returns boolean
4 not in my_list 

#reordering a list + does not change it
my_list =[1,24,8,2
sorted(my_list)
list(reversed(my_list)) # turns reversed object into a list
list(reversed(sorted(my_list)))
