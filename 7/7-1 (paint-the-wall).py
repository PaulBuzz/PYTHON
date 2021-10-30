import math

print("Let's paint the wall and decide how many cans of paint we actually need.")

def paint_calc(height, width, cover):
    area = height * width
    # math.ceil is used to upscale the result and we need it in this particular case to have enough paint
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
