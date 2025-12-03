data = open("day03.txt").read().strip()

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

data = [i for i in data.split('\n')]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1

res = []
for num in data:
    maxjoltage = ""
    currentnum = num
    for digits in range(2):
        for i in range(9, -1, -1):
            if digits:
                f = currentnum.find(str(i))
            else:
                f = currentnum[:- 1].find(str(i))
            if f != -1:
                maxjoltage += str(i)
                currentnum = currentnum[f + 1:]
                break
    res.append(int(maxjoltage))

print("Part one: ")
print(sum(res))

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

res = []
for num in data:
    maxjoltage = ""
    currentnum = num
    for digits in range(13):
        for i in range(9, -1, -1):
            if digits == 12:
                f = currentnum.find(str(i))
            else:
                f = currentnum[:-(11-digits)].find(str(i))
            if f != -1:
                maxjoltage += str(i)
                currentnum = currentnum[f + 1:]
                break
    res.append(int(maxjoltage))

print("Part two: ")
print(sum(res))
