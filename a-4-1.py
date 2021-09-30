import random
print("Let's flip a coin")

rand_int = random.randint(0, 1)
print(rand_int)

if rand_int == 0:
    print("It's Tails!")
else:
    print("It's Heads!")


colors = ["red", "green", "yellow", "blue", "orange", "white"]

colors[0] = "radt"
# меняет значение слова в списке, счет, как и везде, с нуля
colors.append("pink")
# добавляет 1 слово к списку в конце
colors.extend["black", "violet"]
# добавляет список к списку в конце
