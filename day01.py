depth_list = open("input01").readlines()
old = int(depth_list[0])
inc = 0
for depth in depth_list:
    depth = int(depth)
    if depth > old:
        inc += 1
    old = depth

i = 0
inc2 = 0
def sum_measures(d, i):
    return sum(map(lambda s:int(s), d[i:i+3]))
while (i + 3 <= len(depth_list) - 1):
    A = sum_measures(depth_list, i)
    B = sum_measures(depth_list, i+1)
    if B > A:
        inc2 += 1
    i += 1


print(f"Part 1: {inc}")
print(f"Part 2: {inc2}")