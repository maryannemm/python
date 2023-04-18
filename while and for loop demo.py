#while loop demo
num = int(input("enter your age here "))
while num < 18 or num == 18:
    print('invalid', num)
    num= num + 1 # or num += 1
############################################
#### For Loop Demo
names=["tay", 'fay', 'may', 'nay']
for i in names:
    if names == 'may':
        break
    print(names)

