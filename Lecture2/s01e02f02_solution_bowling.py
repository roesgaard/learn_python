def score(frames):
    rolls = []
    for roll_index in range(0, len(frames)):
        if   frames[roll_index] == '-': pins_down = 0
        elif frames[roll_index] == '/': pins_down = 10 - rolls[roll_index-1]
        elif frames[roll_index] == 'X': pins_down = 10
        else:                           pins_down = int(frames[roll_index])
        rolls.append(pins_down)

    points = []
    roll_index = 0
    frame = 0
    while frame < 10:
        if rolls[roll_index] == 10:
            points.append(10 + rolls[roll_index + 1] + rolls[roll_index + 2])
            roll_index += 1
            frame += 1
        elif rolls[roll_index] + rolls[roll_index+1] == 10:
            points.append(10 + rolls[roll_index + 2])
            roll_index += 2
            frame += 1
        else:
            points.append(rolls[roll_index] + rolls[roll_index + 1])
            roll_index += 2
            frame += 1

    return sum(points)


def test(rolls, expected):
    actual = score(rolls)
    print(f"{rolls:24} Expected: {expected:3} Actual: {actual:3} {'OK' if expected == actual else 'ER'}")


test("11111111111111111111", 20)
test("21111111111111111111", 21)
# miss
test("-1111111111111111111", 19)
test("--111111111111111111", 18)
# spare
test("1/------------------", 10)
test("1/1-----------------", 12)
test("1/11----------------", 13)
test("-/------------------", 10)
# last spare
test("-------------------/1", 11)
# strike
test("X------------------", 10)
test("X1-----------------", 12)
test("X11----------------", 14)
test("X51----------------", 22)
test("------------------X12", 13)
test("------------------XXX", 30)

# from https://codingdojo.org/kata/Bowling/
test("XXXXXXXXXXXX", 300)
test("9-9-9-9-9-9-9-9-9-9-", 90)
test("5/5/5/5/5/5/5/5/5/5/5", 150)
