from math import * #imports all math functions eg squareroot etc here
name = input("enter your name ")
name = name.strip() #removes spaces before and after the text. rstrip() from right, lstrip() from left you can specify text to remove in the brackets
print("Your name is ", name)
print("Hello there", name)
age = input("What is your age?")
padding = age.center(10, ' ')
age = int(age)
tab = "G\to\to\td\tm\to\tr\tn\ti\tn\ti\tg"#create tabs within letters
intro="hello {} age {}"
space = name.ljust(30) #creates 30 spaces between name and the next text rjust () has the opposite effect
name=name.strip() #removes spaces around the inputed string
print( "Hello", name, "age:", age)
print(name[3])#prints the 4th letter
print(name[0:5])#prints the defined text
print(name.upper())#turns text to upper case
print(name.lower())#turns text to lowercase can also use casefold()method
print(name.islower())#checks if the entire name is lowercase
print(name.swapcase())#swaps upper and lower cases
#print(age.isdigit())#checks if the age is a digit
print(name.capitalize())#makes the first letter capital i.e title ()function does the same thing
print(name[1:8].lower().islower())#.lower functuion turns the rest of the sentence lowercase
print(len(name))#prints the length of the name
print(len(name) + age)
print(name.isprintable())#characters in the input are printable
print(intro.format(name, age))
print(max(len(name), age))# returns the highest value
print(name.index("a"))# returns the position of the specified value
print(name.replace('m','M'))#to replace m with v, start with the one you want to replace withm
print(type(age), type(name))#to get the data types
print(bin(age + len(name)))#to get the binary of a number can be used without importing
print('this is a squareroot demo ',sqrt(age + len(name)))
print(name.encode())
print(name.endswith('i'))#finds the very last letter
print(space, "youre here")
print(name.find("anne"))#finds the first occurence of the specified name in int
print(name.isascii())#returns true if name is betweena-z
print(tab.expandtabs(4),name)#create tabs between letters
print( "the letter /'e' is repeated ", name.count('e'), "times coutersy of count() fuction") # can use format count (value, start, end) start and end being the positions aka int
print("this is a center() fuction demo", padding)
#rfind()/ rindex () methods find the last occurrence of the specified value syntax: string.rfind(value{Required. The value to search for}, start{Optional. Where to start the search. Default is 0}, end{Optional. Where to end the search. Default is to the end of the string})