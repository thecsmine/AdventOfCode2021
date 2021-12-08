dir_list = open("input02").readlines()
depth = 0
horiz = 0
def f(s):
    tup = s.replace("\n", "").split(" ")
    return (tup[0], int(tup[1]))
dir_list = list(map(f, dir_list))

# Part 1
for (direction, number) in dir_list:
    if direction == "forward":
        horiz += number
    elif direction == "up":
        depth -= number
    else:
        depth += number
print(f"Part 1: {depth * horiz}")

# Part 2
horiz = 0
depth = 0
aim = 0
for (direction, number) in dir_list:
    if direction == "forward":
        horiz += number
        depth += aim * number
    elif direction == "up":
        aim -= number
    else:
        aim += number
print(f"Part 2: {depth * horiz}")