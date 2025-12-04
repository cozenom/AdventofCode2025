data = open("day04.txt").read().strip()
data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

data = [i for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

xlen, ylen = len(data[0]), len(data)


def get_adjacent(x: int, y: int, maxx: int = xlen - 1, maxy: int = ylen - 1, minx: int = 0, miny: int = 0):
    res = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if minx <= nx <= maxx and miny <= ny <= maxy:
                res.append((nx, ny))
    return res


def check_adjacent(x, y, data):
    adj = get_adjacent(x, y)
    if len(adj) < 4:
        return True
    else:
        res = 0
        for pos in adj:
            res += data[pos[1]][pos[0]] == '@'
    if res < 4:
        return True
    else:
        return False


res = []
for y in range(ylen):
    for x in range(xlen):
        if data[y][x] == '@':
            if check_adjacent(x, y, data):
                res.append([x, y])

print(len(res))


def draw(xlist, currentstate):
    for x, y in xlist:
        currentstate[y] = currentstate[y][:x] + 'x' + currentstate[y][x + 1:]
    [print(i) for i in currentstate]


# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")


# Simple solution
def update(xlist, currentstate):
    new = currentstate
    for x, y in xlist:
        new[y] = new[y][:x] + '.' + new[y][x + 1:]
    return new


removed = 0
step = 0
current_state = data.copy()
all_states = []
while True:
    all_states.append(current_state)
    changes = []
    removed_start = removed
    for y in range(ylen):
        for x in range(xlen):
            if current_state[y][x] == '@':
                if check_adjacent(x, y, current_state):
                    changes.append([x, y])
    current_state = update(changes, current_state)
    step += 1
    removed += len(changes)
    if removed_start == removed: break

print(removed)
