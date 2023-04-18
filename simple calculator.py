f_num= float(int(input('enter a number')))
l_num= float(int(input('enter another number')))
op= input('enter an operator')
if op == '+':
    print(f_num+l_num)
elif op == '-':
    print(f_num-l_num)
elif op == '*':
    print(f_num*l_num)
elif op == '/':
    print(f_num/l_num)
else:
    print('invalid operator or number')
