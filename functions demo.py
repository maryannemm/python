def greetings():
    name= str(input("enter your name: "))
    agesss =int(input ("Enter your age"))
    print("Welcome, " + name +" "+ str(agesss)+". we're all crazy here")
greetings() #call the function so that it can be executed

def hello(*names):
    print("Hello "+names[2]+ " you are: ")
hello("amy", "cynthia", "carlene")
###############################################################
#### Return statement. it marks the end of  the code
def add2_numbers():
    num1 = int(input("enter the first number "))
    num2 = int(input("enter the second number "))
    return num1 + num2
print(add2_numbers())
############################################################
###  IF statement
first= int(input("enter your age: "))
lowestage =23
items =("car", "pen", "shoe", )
if  first >= lowestage and first< 100:
    print("You're approved")
elif first < 18 or first<0: 
    print ("not approved")
elif first >= 100:
    print("you're too old")
elif type(first) is not str:
    print("please enter a string")
else:
    print(" still young")
    
