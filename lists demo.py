items = ['car','pen', 'phone', 'laptop', 'phone','paper', 'paper']
things = list(("car", True, 23))
items2= items.remove('phone')
items2[0]='shoes'
print(items2)
print(items[3][0:2])#prints the letter of the first element 
print(items)
print(things)
print(items.insert(1 ,"cube"))
print(items.append("cube"))
print(items.index("pen"))