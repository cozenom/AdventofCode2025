data = open("day09.txt").read().strip()
# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

data = [[int(j) for j in i.split(',')] for i in data.split('\n')]
xmin, xmax, ymin, ymax = min([i[0] for i in data]), max(i[0] for i in data), min(i[1] for i in data), max(
    i[1] for i in data)
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

maxarea = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        x1, y1 = data[i]
        x2, y2 = data[j]
        x, y = abs(x1 - x2) + 1, abs(y1 - y2) + 1
        maxarea = max(maxarea, x * y)

print(maxarea)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")

# Get border
border = set()
last = data[-1]
for x, y in data:
    if last[0] == x:
        for i in range(min(y, last[1]), max(y, last[1])):
            border.add((x, i))
    elif last[1] == y:
        for i in range(min(x, last[0]), max(x, last[0])):
            border.add((i, y))
    border.add((x, y))
    last = [x, y]

# Cache border crossing x coordinate per row
from collections import defaultdict
border_crossings = defaultdict(list)
for x,y in border:
    if (x-1,y) not in border:
        border_crossings[y].append(x)


def is_inside(x, y):
    if (x,y) in border: return True
    crossings = sum(1 for v in border_crossings[y] if v > x)
    return crossings % 2 == 1


from tqdm import tqdm

maxarea = 0
for i in tqdm(range(len(data))):
    x1, y1 = data[i]
    for j in range(i + 1, len(data)):
        x2, y2 = data[j]

        valid = True
        # RAY CASTING INSIDE CHECK
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if not is_inside(x1, y):
                valid = False
                break
            if not is_inside(x2,y):
                valid = False
                break

        if valid:
            x, y = abs(x1 - x2) + 1, abs(y1 - y2) + 1
            maxarea = max(maxarea, x * y)

print(maxarea)
