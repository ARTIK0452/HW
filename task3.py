x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if 1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8:
    c = (x2-x1)**2 + (y2-y1)**2
    if c == 5**2 + 2**2:
        print('YESSS!')
    else:
        print('No no')
