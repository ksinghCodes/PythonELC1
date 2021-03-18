#!/usr/bin/env python 3.7

# ord('a') returns unicode

#chr(97) returns the character a

#Useful Methods

my_str = ' TeStIng'
#my_str.lower() >>> testing
#my_str.upper() >>> TESTING
#my_str.capitalize() >>> Testing 
#"This is a multiword string".title() >>> This Is A Multiword String

# ^ useful to compare email address in boolean

# my_str.isascii() >>> boolean if in ascii  
# my_str.isupper >>> check if its upper , can also do lower/title
# my_ster.isspace

# "2".isdecimal >>> whole number in decimal notation
# "1".isdigit() >>> ^
# "1.0"isnumeric() >>> ^ 
 
# "asdf".isalpha()  >>> true
# "3234asdfds.".isalnum() >>> true ^ and true 

# .isIdentifer checks to see if usable as variable , function , method name etc
# .isPrintable >>> false if \n included


# strings can be tokens 
phrase = "This is a simple phrase"
words = phrase.split()
# ['This', 'is', 'a', 'simple', 'phrase']
url = "https://example.com/users/jimmy"
user = url.split('/')[-1] # seperate with slash, get the last one of the list

", ".join(words) 

#use example
lines = ['First line', 'Second line', 'Third line']
output ='\n'.join(lines)
# addes \n to all indexes
prints(output)
# First line
# Second line
# Third line

template = " Hello, my name is {}, and I really enjoy {}, Have a nice day!"
template .format('Keith', 'Python')
# format inserts keith and python into curly brakcets
# or my name is {0} ... enjoy {1} .. day!- {0}



