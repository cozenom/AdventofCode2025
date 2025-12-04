data = open("day04.txt").read().strip()
# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

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


def draw(removelist, currentstate):
    for x, y in removelist:
        currentstate[y] = currentstate[y][:x] + 'x' + currentstate[y][x + 1:]
    return currentstate


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
all_states.append([f"Step 0"] + current_state.copy())
while True:
    all_states.append([f"Step {step}"] + current_state.copy())
    changes = []
    for y in range(ylen):
        for x in range(xlen):
            if current_state[y][x] == '@':
                if check_adjacent(x, y, current_state):
                    changes.append([x, y])

    current_state = update(changes, current_state)
    step += 1
    removed += len(changes)
    if not changes: break
    all_states.append([f"Step {step}"] + draw(changes, current_state.copy()))

all_states.append([f"Step {step}"] + current_state.copy())

print(removed)

# Vis - TAKES A WHILE WITH FULL INPUT

from PIL import Image, ImageDraw, ImageFont

def grid_to_image(grid, char_size=12, padding=10):
    width, height = (len(grid[1]) * char_size) + (2 * padding) + char_size, (len(grid) * char_size) + (
            2 * padding) + char_size
    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("JetBrainsMono-Regular.ttf", char_size)
    except:
        font = ImageFont.load_default()

    y_pos = padding
    for row in grid:
        x_pos = padding
        for char in row:
            if char == '@':
                draw.text((x_pos, y_pos), char, fill='green', font=font)
            elif char == '.':
                draw.text((x_pos, y_pos), char, fill='white', font=font)
            elif char == 'x':
                draw.text((x_pos, y_pos), char, fill='red', font=font)
            else:
                draw.text((x_pos, y_pos), char, fill='white', font=font)
            x_pos += char_size
        y_pos += char_size
    return img


def create_ascii_gif(frames, fname="day04.gif"):
    pillow_frames = []
    for frame in frames:
        img = grid_to_image(frame)
        pillow_frames.append(img)

    pillow_frames.insert(-1, pillow_frames[-1])
    pillow_frames[0].save(fname, save_all=True, append_images=pillow_frames[1:], duration=400, loop=1)

create_ascii_gif(all_states)
