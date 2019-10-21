operand = ['+', '-', '*', '/']
print()
a = input()
b = input()
c = str(input())
if c in operand and b != '0':
    print(eval(a+c+b))
else:
    print('ЫЫЫЫЫЫ')
