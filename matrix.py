size_matrix = int(input())
number = int(input())
number1 = [i for i in range(1,number+1)]
print(number1[0])
print(' ')

list_db = [[number1] * size_matrix for i in range(size_matrix)]
    
for i in range(size_matrix):
    for j in range(size_matrix):  
        print(list_db[i][j], end='   ')
    print()
