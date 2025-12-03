data = open("day02.txt").read().strip()

# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

data = [[int(j) for j in i.split("-")] for i in data.split(',')]
print(data)

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
# Length of strings is never more than 1 apart :)

res = []
for left, right in data:
    llen = len(str(left))
    if llen % 2 == 1:
        current = 10 ** (llen // 2)
    else:
        current = int(str(left)[:llen // 2])

    while True:
        invalid = int(str(current) + str(current))
        if invalid > right:
            break
        if invalid >= left:
            res.append(invalid)
        current += 1

print("Part one: ")
print(sum(res))

# ----------------------------------------------------------------------------------------------------------------------
# Part 2

res = []
for left, right in data:

    for i in range(left, right+1):
        i = str(i)
        for r in range(len(i)):
            window = i[0:r]
            if i.replace(window, "") == "":
                res.append(int(i))
                break

print("Part two: ")
print(sum(res))
