string = input()
i = 0
while i < len(string):
    if string[i] == '.':
        break
    print(string[i])
    i = i + 1
else:
    print('Точки нет')
