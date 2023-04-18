file = open('C:/Users/kille/python/write file.txt', 'w')
file3= open('C:/Users/kille/python/countries chinese.txt','a')
file2= open('C:/Users/kille/python/anotherfile.txt', 'w')#craetes another file
file.write("this is a second list of countries and their chinese names:")
file2.write('this is just another file')
file3.write("\n this is another line")

#####################################
program = open('C:\\Users\\kille\\python\\new.py', 'w')# use double backslashes when creating a python code
program.write("print(\"hello there\")")
program.close()
file.close()
file2.close()
file3.close()