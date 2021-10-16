from typing import Reversible

print("What your cartoon name would be? Let's check!\n")
fruit = input("What is your favourite fruit?\n")
animal = input("What is your favourite animal?\n")
print("Your cartoon name is: " + fruit[::-1] + " " + animal[::-1])
# [::-1] - реверс слова в строке
