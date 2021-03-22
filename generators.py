#!/usr/bin/env/python 3.7


#Generators - functions acting like iterators - like range
def gen_range(stop,start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step 


generator = gen_range(10)

print(next(generator) ) # each tiem next generator is called num goes up one

# or more practicaly use in a for loop

for num in gen_range(10, step=2):
    print(num)
    
    # for loop conintues calling next

#castable as list




