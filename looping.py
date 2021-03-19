#!/usr/bin/env/python 3.7

#Loooopppppiiiinnnnggg

#while Condition:
#----code

count1 = 1
while count1 < 10:
    print("looping")
    count1 += 1



#for TEMP_VARIABLE in SEQUENCE:
#----pass

colors = ['blue','red','green','purple']
for color in colors:
    print(color)

ages = {'kevin': 59, 'bob': 40, 'kayla': 21} 

#default only prints key
for key in ages:
    print(key)

# pass tuple to unpack
for key, value in ages:
    print(key, value)

#NEsting and combing loops/condtionals

counter = 1 
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1
#############################

#break and continue

count = 0
while count < 10:
    ## if even
    if count % 2 ==0:
        #incrmeent and skip printing
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    #still need to increment odd numbers
    count += 1
###############
    
count2 = 0
while  count2< 10:
    ## if even
    if count2 % 2 ==0:
        #if true exit loop
        break
    print(f"We're counting odd numbers: {count2}")
    #still need to increment odd numbers
    count += 1

########    ########

# Else with loops - execute additional line upon loop completion
# good for use with breaks

colors2 = ['red','pink','blue','organe','green']
for color in colors2:
    if color == 'orange':
        print('Organge is in the list')
        break
        #orange is found exit loop
else:
    print('Orange is not in the list')
    # orange was never found loop is done. 
####################

# ranges - immutable
# use for iterating a for loop x times . or easy standin for creatin list

# these codes are equal.
count3 = 1
while count3 <= 4:
    print("looping")
    count3 += 1
# or 
for _ in range(4):
    # range ( 0, 4, 1) = range (0,4)= range(4) (start, go up to, increment)
    print("looping")

#######################################

# list comprehensions - modify list into another list

# less efficient way
# make two lists, use for loop , take indexes , set modify into other list
colorsx3 = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colorsx3 = []
for color in colorsx3:
     uppercase_colorsx3.append(color.upper())

# uppercase_colors
# ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

# or list comprehension way

colorsx4 = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colorsx4 = [color.upper for color in colorsx4]
# or you can also filter, variable for variable in set if variable is in this set too
warm_colors = [color for color in colorsx4 if color in ['red','orange','yellow']]
