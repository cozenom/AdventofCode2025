data = open("day05.txt").read().strip()
# data = """"""

data = [[j for j in i.split("\n")] for i in data.split('\n\n')]
ranges = [[int(j) for j in i.split('-')] for i in data[0]]
ingredients = [int(i) for i in data[1]]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

fresh = []
for ingredient in ingredients:
    if any(low <= ingredient <= high for low, high in ranges):
        fresh.append(ingredient)

print(len(fresh))
# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")

ranges_sorted = sorted(ranges, key=lambda x: x[0])
ranges_merged = [ranges_sorted[0]]
for i in range(1, len(ranges_sorted)):
    last = ranges_merged[-1]
    curr = ranges_sorted[i]

    if curr[0] <= last[1]:
        last[1] = max(last[1], curr[1])
    else:
        ranges_merged.append(curr)

res = sum(hi-lo+1 for (lo,hi) in ranges_merged)
print(res)
