# for num in range(1, 101):
#     txt = ""
#     if num % 3 == 0:
#         txt += 'Fizz'
#         # print(end="Fizz")
#     if num % 5 == 0:
#         txt += 'Buzz'
#     if txt == '':
#         txt = num
#     print(txt)
# best solution

for num in range(1, 101):
    if num % 3 == 0:
        print(end="Fizz")
    if num % 5 == 0:
        print(end="Buzz")
    print(num)
