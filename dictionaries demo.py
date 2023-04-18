#i.e dictionaries dont allow duplication
my_dict = {
    'name': "maryanne",
    'age':26 ,
    'group': "girls",
    'friends':['isha','carlene', 'Cynthia']
}
print("hello ", my_dict['name'], "Your age is: ", my_dict['age'])
print(my_dict['friends'])
print(type(my_dict))
x= my_dict['friends']
print("Your friends are",x)