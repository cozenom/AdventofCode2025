data = open("day11.txt").read().strip()

# p1
# data = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""

# p2
# data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""

d = {i[0]: i[1].split(' ') for i in [[j for j in i.split(": ")] for i in data.split('\n')]}
# ----------------------------------------------------------------------------------------------------------------------
# Part 1
print("Part one: ")


def dfs(node, path=[]):
    next = d[node]
    if next == ['out']:
        return [path]
    all_paths = []
    for i in next:
        all_paths += dfs(i, path + [i])
    return all_paths


print(len(dfs('you')))

# ----------------------------------------------------------------------------------------------------------------------
# Part 2
print("Part two: ")

from functools import cache


@cache
def dfs2(node, dac=False, fft=False):
    next = d[node]
    if next == ['out']:
        return 1 if (dac and fft) else 0
    if node == 'dac': dac = True
    if node == 'fft': fft = True

    total = 0
    for i in next:
        total += dfs2(i, dac, fft)
    return total

print(dfs2('svr'))