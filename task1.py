message = str(input("Ввод: "))
cost = round((len(message) * 0.23), 2)
coststr = str(cost).split('.')
print(coststr[0],'р.',coststr[1],'коп.')


