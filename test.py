import os

filename = 'C:/Users/kille/python/reading demo.txt'

if os.path.exists(filename):
    file = open(filename, 'r')
    print(file)
    # r means i want to read this file. cant write or append. theres also 'w' for write, 'a' for append at the end of the list, "w+r" for read and write
    print(file.readable())# confirm if we have access to the file.
    print(file.readline())# prints the first line
    lines = file.readlines() # puts the data in a list
    file.close() # always ensure to close file

    find = input('Enter the country name: ')
    find = find.capitalize()

    # Reset the file pointer to the beginning of the file
    file = open(filename, 'r')
    line_num = 1
    for country in lines:
        # Remove the newline character at the end of the line
        country = country.strip()
        if country == find:
            print('Country found at index', line_num)
            break
        line_num += 1

    file.close() # always ensure to close file
else:
    print(f"The file '{filename}' does not exist.")
