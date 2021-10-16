import random
number = random.randint(1, 100)
for i in range(5):
    a = int(input())
    if a < number:
        print('Маловато будет.')
    elif a > number:
        print('Перебрал.')
    elif a == number:
        print('Молодца!')
        break
else:
    print('Ха-ха, проиграл.')
