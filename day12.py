data = open("day12.txt").read().strip()

# data = """0:
# ###
# ##.
# ##.
#
# 1:
# ###
# ##.
# .##
#
# 2:
# .##
# ###
# ##.
#
# 3:
# ##.
# ###
# ##.
#
# 4:
# ###
# #..
# ###
#
# 5:
# ###
# .#.
# ###
#
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2"""

data = [data.split('\n\n')[:-1]] + [[[[int(k) for k in j[0].split('x')]] + [[int(k) for k in j[1].split()]] for j in [i.split(": ") for i in data.split('\n\n')[-1].split('\n')]]]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

sizes = {int(i[0]): i.count('#') for i in data[0]}

res = 0
for [x,y], requirements in data[1]:
    area = x*y
    for i in range(len(requirements)):
        area -= requirements[i] * sizes[i]
    if area > 0:
        res += 1

print(res)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")



print()
