# this file should be in the same folder as this program for easier access coppy path with foward slash
file = open('C:/Users/kille/python/reading demo.txt', 'r')
# r means i want to read this file. cant write or append. theres also 'w' for write, 'a' for append at the end of the list, "w+r" for read and write
print(file.readable())# confirm if we have access to the file.
print(file.readline())# prints the first line
file=file.readlines()# puts the data in a list
for country in file:
    print(country)
