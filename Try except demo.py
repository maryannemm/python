## Error handling in python
try:
    yob= input('enter your year of birth: ')
    if len(yob) != 4:
        print('invalid length')
    else:
        yob= int(yob)
        print(yob)
except:
    print('something went wrong. try again! ')