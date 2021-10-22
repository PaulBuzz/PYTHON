string = input()
i = 0
while i < len(string):
    if string[i] == '.':
        break
    print(string[i])
    
else:
    print('Точки нет.')
