data = open("day08.txt").read().strip()
# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

data = [[int(j) for j in i.split(',')] for i in data.split('\n')]

print(data)
print(len(data))
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")

edges = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):  # i+1 to avoid duplicates
        x1, y1, z1 = data[i]
        x2, y2, z2 = data[j]
        dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2  # sq distance is cheaper
        edges.append((dist_sq, i, j))
edges_sorted = sorted(edges, key=lambda x: x[0])

groups = [[edges_sorted[0][1], edges_sorted[0][2]]]
for i in range(1, 1000):
    _, a, b = edges_sorted[i]
    newgroups = []
    tomerge = []
    for g in groups:
        if a in g and b in g:
            tomerge.append(g)
        elif a in g:
            tomerge.append(g + [b])
        elif b in g:
            tomerge.append(g + [a])
        else:
            newgroups.append(g)
    if len(tomerge) == 2:
        newgroups.append(list(set(tomerge[0] + tomerge[1])))
    elif len(tomerge) == 1:
        newgroups.append(tomerge[0])
    else:
        newgroups.append([a, b])
    groups = newgroups

groups = sorted(groups, key=lambda x: len(x), reverse=True)

res = 1
for i in groups[:3]:
    res *= len(i)

print(res)

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")






print()
