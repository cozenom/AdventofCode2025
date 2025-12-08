data = open("day07.txt").read().strip()
# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

data = [i for i in data.split('\n')]
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

xmax = len(data[0])
beams_x = {data[0].find('S')}

splits = 0
for row in data[1:]:
    newbeams = set()
    for x in beams_x:
        if row[x] == '^':
            splits += 1
            if x + 1 < xmax: newbeams.add(x + 1)
            if x - 1 > 0: newbeams.add(x - 1)
        else:
            newbeams.add(x)
    beams_x = newbeams
print(splits)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")
from collections import defaultdict

beamlocs = {0: {data[0].find('S'): 1}}

ymax = len(data)
for y in range(1, ymax - 1):
    currentlocs = beamlocs[y - 1]
    currentrow = data[y]
    newlocs = defaultdict(int)
    for x,count in currentlocs.items():
        if currentrow[x] == '^':
            newlocs[x - 1] = newlocs[x - 1] + count
            newlocs[x + 1] = newlocs[x + 1] + count
        else:
            newlocs[x] = newlocs[x] + count
    beamlocs[y] = newlocs

print(sum([beamlocs[ymax-2][i] for i in beamlocs[ymax-2].keys()]))
