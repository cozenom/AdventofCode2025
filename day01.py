data = open("day01.txt").read().strip()

# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

data = [[i[0], int(i[1:])] for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
pos = 50
password = 0
for i in data:
    if i[0] == 'R':
        pos += i[1]
    else:
        pos -= i[1]
    pos = pos % 100
    if pos == 0:
        password += 1

print("Part one: ")
print(password)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2

pos = 50
password = 0
for i in data:
    oldpos = pos
    if i[0] == 'R':
        pos += i[1]
    elif i[0] == 'L':
        pos -= i[1]
    #print(f'pos: {pos}, oldpos: {oldpos}')

    # Add for crossing 0
    if pos < 0 < oldpos:
        password += 1

    # Add rotations > 100
    if (abs(pos) // 100) > 0:
        password += abs(pos) // 100

    # Add pointing at 0
    if pos == 0:
        password += 1

    pos = pos % 100


print("Part two: ")
print(password)
