#ГОТОВО 1. Дописать шифр Цезаря: реализовать "переполнение" алфавита (z -> a)
#НЕ ГОТОВО ПО ТЕХНИЧЕСКИМ ШОКОЛАДКАМ!
#ГОТОВО 3. Работоспособность с буквами верхнего регистра
#ГОТОВО4. Работоспособность с цифрами (0 ... 9 -> 0)

    
class Ceasar:
    def __init__(self):
        self.input = input()
        self.shift = int(input())
        self.cypher()
    
    def cypher(self):
        res = ""
        res1 = ""
        res2 = ""
        res3 = ""
        res4 = ""
        res5 = ""
        for i in range(len(self.input)):
            if ord(self.input[i]) >= ord('a') and ord(self.input[i]) <= ord('z'):
                res += chr(ord(self.input[i]) + self.shift)
        print(res)

        for i in range(len(self.input)):
            if ord(self.input[i]) >= ord('A') and ord(self.input[i]) <= ord('Z'):
                res1 += chr(ord(self.input[i]) + self.shift)
        print(res1)



        for i in range(len(self.input)):
            if ord(self.input[i]) <= ord('z') and ord(self.input[i]) >= ord('a'):
                res2 += chr(ord(self.input[i]) - self.shift)
        print(res2)

        for i in range(len(self.input)):
            if ord(self.input[i]) <= ord('Z') and ord(self.input[i]) >= ord('A'):
                res3 += chr(ord(self.input[i]) - self.shift)
        print(res3)

        for i in range(len(self.input)):
            if ord(self.input[i]) >= ord('0') and ord(self.input[i]) <= ord('9'):
                res4 += chr(ord(self.input[i]) + self.shift)
        print(res4)

        for i in range(len(self.input)):
            if ord(self.input[i]) <= ord('9') and ord(self.input[i]) >= ord('0'):
                res5 += chr(ord(self.input[i]) - self.shift)
        print(res5)
test = Ceasar()
