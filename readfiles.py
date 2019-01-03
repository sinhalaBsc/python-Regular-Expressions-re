# this lesson show how to read text skill file in python.

'''
for open the file from your computer you can use python build-in open command.let's open 'text.txt'
file that located on same directory have current python file.There are two mathod to open files.

1. nomal method.
f=open('text.txt') # pass the directory as parameter
                   # this command defaults opening to file for reading. but
                   # we can set that for reading,writing,appending or reading/writing

# let's specifies that we open this file for reading in for same command
f=open('text.txt','r')  #  read 'r'
                        #  write 'w'
                        #  append 'a'
                        #  read/write 'r+'

# in case we opened file should colse when we no need more, to not for messive with others.
f.close()
                   
# just print the file name that we opened.
print(f.name)
# >> text.txt

# just print which mode we opened the current file.
print(f.mode)
# >> r

eg:
'''
f=open('text.txt','r')
print(f.name)
print(f.mode)
f.close()

'''
2. context manager method

with open('text.txt','r') as f:       # 'f' is variable name of opened file.
    print(f.name)                     #  benefit of this method is it will automatically close
                                      #  when we exit from block context and clean exceptions which are thrown.

# method_1 : for read text file (load all text file data to 'f_contents' variable)
with open('text.txt','r') as f:
    f_contents=f.read()          # this method good for read small data text file.
    print(f_contents)

# method_2 : for read text file (load all text file data to 'f_contents' by lines)
with open('text.txt','r') as f:
    f_contents=f.readlines()     # this method good for small data text file.
    print(f_contents)            # this will add '\n' to every end of lines data.

# method_3 : for read text file (load one data line to 'f_contents' variable from file)
with open('text.txt','r') as f:
    f_contents=f.readline()      # this method good for big data text file.
    print(f_contents)            # print only one line from text file.   

    f_contents=f.readline()      # this will load only next line data from last read's line.
    print(f_contents)            # by every this command(method) will print next line data from file.

    f_contents=f.readline()      
    print(f_contents,end='')     # pass end='' to escape printing extra new line.
                                 # for same purpose we can use print(f_contents[:-1]) 


# for read all of the content from an extremely large file with less memory using.
# method_4 : for read text file (use for loop for load line by line)
with open('text.txt','r') as f:
    for line in f:
        print(line,end='')
# method_5 : for read text file (use for loop for load line by line)        
with open('english.txt','r') as f:
    f_contents=f.readline()
    while f_contents:
        getdata(f_contents,f.tell())
        f_contents=f.readline()

        

# ********* more control **********

# method_6 : for read text file (load frist 100 characters form the file)
with open('text.txt','r') as f:
    f_contents=f.read(100)      # use only frist 100 characters form the file.
    print(f_contents,end='')    # this will add '\n' to every end of lines data.

    f_contents=f.read(100)      # use only next 100 characters form the file.
    print(f_contents,end='')      

    f_contents=f.read(100)      # if there don't have any more characters then.  
    print(f_contents,end='')    # print nothing.

# method_7 : for read text file (print all from loading by 100 characters at one time form the file)
with open('text.txt','r') as f:

    size_to_read =100

    f_contents=f.read(f_contents)

    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(f_contents)

# to print current position on the text file
print(f.tell())

# to change flow of position when we want
f.seek(0)   #  file go to 0 chareater

eg:
'''
with open('text.txt','r') as f:

    size_to_read =10
    
    f_contents=f.read(size_to_read)      
    print(f_contents,end='')            

    f.seek(0)                           # set current posintion to 0 character
    
    f_contents=f.read(size_to_read)      
    print(f_contents,end='')      

# >> 1) This is1) This is

