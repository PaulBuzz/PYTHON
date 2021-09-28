print('Че надеть че надеть?')
print('А сколько градусов?')
t = int(input())
if t < -4:
    print('Надевай шубу')
elif t > -4 and t < 0:
    print('Напяливай теплую куртенку')
elif t >= 0 and t < 12:
    print('Влезай в легкий тренч')
elif t >= 12 and t < 27:
    print('Кофта за 300 грн - топчик')
else:
    print('Майка - заебок')
