# This library should import for work with regular expression
import re

# you can use following syntec for multiple line in python.it's call 'multiline string'
# ''' my multiline string'''


text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

all special characters in keyboard
~ ` ! @ # £ € $ ¢ ¥ § % ° ^ & * ( ) - _ + = { } [ ] | \ / : ; " ' < > , . ?

MetaCharacters Needs to be escapesd
. ^ $ * + ? { } [ ] \ | ( )

321-654-0987
123.456.7890

Mr. Piyasiri
Mr Pasindu
Ms word
Mrs Rathnayaka
Mr. X

'''

sentence='Start a sentence and then bring it to an end'

# MetaCharacters (we needs to be escapesd by this characters when re.compile(r'.'))
# . ^ $ * + ? { } [ ] \ | ( )

# . - match with all characters in the string
# ^ - match with worng character
# $ - match
# * - error: nothing to repeat at position 0
# + - error: nothing to repeat at position 0
# ? - error: nothing to repeat at position 0
# { - match
# } - match
# [ - error: unterminated character set at position 0
# ] - match
# \ - eol while scaning string literal
# | - match with all characters in the string
# ( - error: missing ), unterminated subpattern at position 0
# ) - error: unbalanced parenthesis at position 0

# we can use '\' before the MetaCharacters to escape eg:-
# >>> pattern=re.compile(r'\.')
# >>> pattern=re.compile(r'sinhala\.ru')




pattern=re.compile(r'\ass')
matches=pattern.finditer(text_to_search)

for m in matches:
    print(m)

print(text_to_search[0:10])

'''
.  - any character Except New Line
\d - Digit (0-9)
\D - Not a Digit (0-9)
\w - Word Character (a-z,A-Z,0-9, _ )
\W - Not a Word Character
\s - Whitespace (space , tab , newline)
\S - Not Whitespace (space , tab , newline)

\b - Word boundary (Matches invisible position before or before)
\B - Not a Word Boundary(Matches Not invisible position before )
^  - From Beginning of a String
$  - To End of a String

[] - Matches Characters in brackets
[^]- Matches Characters Not in brackets

'''

# Word boundary eg:- '\b'
# Matches if there have any invisible position before select-phrase(itc -'Ha')
# start and after positions alwase have invisible position
boundary_b=re.compile(r'\bHa')
bmatches=boundary_b.finditer(' Ha HaHa ') # select ' <Ha> <Ha>Ha '

for b in bmatches:
    print('from b ',b)


# Word boundary eg:- '\B'
# Matches if there not any invisible position before select-phrase(itc -'Ha')
# start and after positions alwase have invisible position
boundary_B=re.compile(r'\BHa')
Bmatches=boundary_B.finditer(' Ha HaHaHa ') # select ' Ha Ha<Ha><Ha> '

for B in Bmatches:
    print('from B ',B)



# From Beginning of a String eg:-'^'
sentence='Start a sentence and then bring it to an end'

fromStart=re.compile(r'^Sta')
smatches=fromStart.finditer(sentence) # select ' Ha Ha<Ha><Ha> '

for s in smatches:
    print('from start ',s)


# To End of a String eg:-'$'
sentence='Start a sentence and then bring it to an end'

toStart=re.compile(r'nd$')
tmatches=toStart.finditer(sentence) # select ' Ha Ha<Ha><Ha> '

for t in tmatches:
    print('to end ',t)


