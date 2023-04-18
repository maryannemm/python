my_2dlist = [ ['car','chair', 'desk'],
             [1, 2, 3],
             [True,False,True]

]
print(my_2dlist)
print(my_2dlist[0:1])
print(my_2dlist[0][1])

for lists in my_2dlist:
    print(lists)
    for rows in lists:
        print(rows)
        if rows == 'car':#### checks if 'car is present in the 2d items list
            
            print (True)
        else:
           break