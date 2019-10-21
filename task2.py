operand = ['+', '-', '*', '/']
a = input()
b = input()
c = str(input())
if c in operand and b != '0':
    print(round(eval(a+c+b), 2))
else:
    print('ЫЫЫЫЫЫ')
