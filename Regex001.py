# This library should import for work with regular expression
import re

# we know that in python string can holder any character as string
# set but '\+cmd' symbol that only way to give commads to string
# eg:- '\n' , '\t' ...ect

#$print('we\nSriLanka')
print('Sri\tLanka')

# but we are using row String in this case to not any charactor effect to
# our given string by python before Regex 
# row string syntax >> r'your string'
#$print(r'Sri\tLanka')


#let's see how to match same letter-character(pattern) in string.
#let's define the pattern for future use.
pattern=re.compile(r'abc')

# this is our string whitch we want to match with
txt ='samadhi abcddd lanka'

# desire pattern with string 
matches=pattern.finditer(txt)
# and this result getting as python object
print(matches)
#>>> <callable_iterator object at 0x7fc7986b9c50>

#let's print the object using for loop
for m in matches:
    print(m)
#>>> <_sre.SRE_Match object; span=(8, 11), match='abc'>
#  it's say's   match='abc' in txt string between span=(8, 11)  (8,11] 
print(txt[8:11])
#>>> abc
