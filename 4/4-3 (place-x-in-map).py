row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horiz = int(position[0])
vert = int(position[1])

map[vert - 1][horiz - 1] = ":)"
print(f"{row1}\n{row2}\n{row3}")
