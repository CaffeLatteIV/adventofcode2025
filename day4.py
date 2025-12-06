import sys
sys.setrecursionlimit(9000)
ata = []
with open('input/day4.txt') as file:
    data = [list(l.strip()) for l in file.readlines()]


def check(l, i, j):
    count = 0
    for k in range(-1, 2):
        if j+k < 0 or j+k >= len(l[i]):
            continue
        for z in range(-1, 2):
            if i+z < 0 or i+z >= len(l):
                continue
            if l[i+z][j+k] == '@':
                count += 1
    return count-1


def forklift():
    res = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@' and check(data, i, j) < 4:
                data[i][j] = 'x'
                res += 1 + forklift()
    return res


print(forklift())
