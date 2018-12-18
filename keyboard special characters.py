
# you can use following syntec for multiple line in python.it's call 'multiline string'
# ''' my multiline string'''

txt='''
~ 	Tilde.
` 	Acute, back quote, grave, grave accent, left quote, open quote, or a push.
! 	Exclamation mark, exclamation point, or bang.
@ 	Ampersat, arobase, asperand, at, or at symbol.
# 	Octothorpe, number, pound, sharp, or hash.
£ 	Pound Sterling or Pound symbol.
€ 	Euro.
$ 	Dollar sign or generic currency.
¢ 	Cent sign.
¥ 	Chinese/Japenese Yuan.
§ 	Micro or Section.
% 	Percent.
° 	Degree.
^ 	Caret or circumflex.
& 	Ampersand, epershand, or and symbol.
* 	Asterisk, mathematical multiplication symbol, and sometimes referred to as star.
( 	Open parenthesis.
) 	Close parenthesis.
- 	Hyphen, minus or dash.
_ 	Underscore.
+ 	Plus.
= 	Equal.
{ 	Open brace, squiggly brackets, or curly bracket.
} 	Close brace, squiggly brackets, or curly bracket.
[ 	Open bracket.
] 	Closed bracket.
| 	Pipe, or, or vertical bar.
\ 	Backslash or reverse solidus.
/ 	Forward slash, solidus, virgule, whack, and mathematical division symbol.
: 	Colon.
; 	Semicolon.
" 	Quote, quotation mark, or inverted commas.
' 	Apostrophe or single quote.
< 	Less than or angle brackets.
> 	Greater than or angle brackets.
, 	Comma.
. 	Period, dot or full stop.
? 	Question mark.'''


ch=''
p=0
for i in txt:
    p+=1
    if  i=='\n':
        ch+=txt[p]
        #print(txt[p])

print(ch)

#>>> ~`!@#£€$¢¥§%°^&*()-_+={}[]|\/:;"'<>,.?
