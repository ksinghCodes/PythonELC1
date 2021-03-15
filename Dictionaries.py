#!/usr/bin/env python 3.7

# Dictionaries - Hashes - Asscoiated Arrays , - Key Pairs

ages = {'Kevin': 59, 'alex': 29, 'bob': 40} 
# VAR = { 'Key' : Value}

# Keys must be immutable types and unique

# subscribing/subscript 
# ages['kevin'] >>> 59

#dictionaries are mutable 
 ages['kayla'] = 21 # appends 
 ages ['kevin'] = 60 # resets
 del ages ['kevin'] # deletes 

# Can still use IN/ not in operations
# alex in ages >>> true

#initialzing
weights = dict(kevin=160, bob=240, kayla=135)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
