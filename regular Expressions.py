# This library should import for work with regular expression
import re

# we know that in python string can holder any character as string
# set but '\+cmd' symbol that only way to give commads to string
# eg:- '\n' , '\t' ...ect

print('we\nSriLanka')
print('Sri\tLanka')

# but we are using row String in this case to not any charactor effect to
# our given string by python before Regex 
# row string syntax >> r'your string'
print(r'Sri\tLanka')

txt ='' 
