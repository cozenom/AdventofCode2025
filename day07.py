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
xlen, ylen = len(data[0]), len(data)
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

beams_x = {data[0].find('S')}

splits = 0
for row in data[1:]:
    newbeams = set()
    for x in beams_x:
        if row[x] == '^':
            splits += 1
            if x + 1 < xlen: newbeams.add(x + 1)
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

maxbeams = 0
for y in range(1, ylen - 1):
    currentlocs = beamlocs[y - 1]
    currentrow = data[y]
    newlocs = defaultdict(int)
    for x, count in currentlocs.items():
        if currentrow[x] == '^':
            newlocs[x - 1] = newlocs[x - 1] + count
            newlocs[x + 1] = newlocs[x + 1] + count
        else:
            newlocs[x] = newlocs[x] + count
    beamlocs[y] = newlocs

print(sum([beamlocs[ylen - 2][i] for i in beamlocs[ylen - 2].keys()]))

# Vis
beamlocs[ylen - 1] = beamlocs[ylen - 2]
maxbeams = max([i for i in beamlocs[ylen - 2].values()])

from PIL import Image, ImageDraw, ImageFont


def get_color(c): # Blue
    if c == 0:
        return (0, 0, 0)

    ratio = min(c / maxbeams, 1.0)

    # Blue -> White
    base_r, base_g, base_b = 50, 150, 255

    r = int(base_r + ratio * (255 - base_r))
    g = int(base_g + ratio * (255 - base_g))
    b = int(base_b + ratio * (255 - base_b))

    return (r, g, b)


# def get_color(c):  # Red
#     if c == 0:
#         return (0, 0, 0)
#
#     ratio = min(c / maxbeams, 1.0)
#
#     if ratio < 0.5:
#         # Dark Red → Bright Red/Orange
#         r = int(150 + ratio * 2 * 105)
#         g = int(ratio * 2 * 150)
#         b = 0
#         return (r, g, b)
#     else:
#         # Orange/Yellow → White
#         r = 255
#         g = int(150 + (ratio - 0.5) * 2 * 105)
#         b = int((ratio - 0.5) * 2 * 255)
#         return (r, g, b)


endstate = [data[0]]
for y, r in beamlocs.items():
    if y == 0:
        continue
    else:
        currentrow = data[y]
        for x in range(xlen):
            if currentrow[x] != '^' and beamlocs[y][x] > 0:
                currentrow = currentrow[:x] + '|' + currentrow[x + 1:]
        endstate.append(currentrow)

states = []
for i in range(ylen):
    states.append(endstate[:i + 1] + data[i + 1:])


def create_ascii_gif(frames, duration=400, fname="day07.gif", final_pause=2000, char_size=12, padding=10):
    width = (xlen * char_size) + (2 * padding)
    height = (ylen * char_size) + (2 * padding)
    try:
        font = ImageFont.truetype("JetBrainsMono-Regular.ttf", char_size)
    except:
        font = ImageFont.load_default()

    pillow_frames = []
    img = Image.new('RGB', (width, height), color='black')

    # Build frames incrementally
    for frame_num in range(len(frames)):
        img = img.copy()
        draw = ImageDraw.Draw(img)

        # Only draw the NEW row (row frame_num)
        if frame_num < ylen:
            y_pos = padding + (frame_num * char_size)
            row = frames[frame_num][frame_num]

            for x in range(xlen):
                x_pos = padding + (x * char_size)
                char = row[x]

                if char == '^':
                    draw.text((x_pos, y_pos), char, fill='green', font=font)
                elif char == '.':
                    draw.text((x_pos, y_pos), char, fill='black', font=font)
                elif char == '|':
                    color = get_color(beamlocs[frame_num][x])
                    draw.text((x_pos, y_pos), char, fill=color, font=font)

        pillow_frames.append(img.copy())

    # Make final frame linger
    pause_frames = final_pause // duration
    for _ in range(pause_frames):
        pillow_frames.append(pillow_frames[-1])

    pillow_frames[0].save(
        fname,
        save_all=True,
        append_images=pillow_frames[1:],
        duration=duration,
        loop=0
    )


create_ascii_gif(states, duration=100, final_pause=3000)
