data = open("day06.txt").read()
# data = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """

data = [i for i in data.split("\n")]
import re

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")
datap1 = [[j for j in re.split(r"\s+", i) if j] for i in data]

import math

xlen, ylen, res = len(datap1[0]), len(datap1), 0

for x in range(xlen):
    numbers = []
    for y in range(ylen):
        if y == ylen - 1:
            if datap1[y][x] == "+":
                res += sum(numbers)
            elif datap1[y][x] == "*":
                res += math.prod(numbers)
        else:
            numbers.append(int(datap1[y][x]))

print(res)
# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")

xlen, ylen = len(data[0]), len(data)
rotated = ["".join([data[y][x] for y in range(ylen)]) for x in range(xlen)]
numbers, res, operator = [], 0, ""
for x in range(xlen):
    row = rotated[x]
    if row[-1] == "*" or row[-1] == "+":
        operator = row[-1]
    if row != " " * ylen:
        numbers.append(int(row[:-1]))
    if row == " " * ylen or x == xlen-1:
        if operator == "*":
            res += math.prod(numbers)
        elif operator == "+":
            res += sum(numbers)
        numbers, operator = [], ""

print(res)
