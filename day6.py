import numpy as np


def getPuzzle1():
    data = []
    with open('input/day6.1.txt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            k = 0
            line = lines[i].strip().split(' ')
            for j in range(len(line)):
                val = line[j]
                if val == '' or val == ' ' or val == '\n':
                    continue
                if i == 0:
                    data.append([val])
                else:
                    data[k].append(val)
                    k += 1
    return data


def calculate(l):
    op = l[-1]
    res = 1
    if op == '+':
        res = 0
    for i in range(len(l)-1):
        val = int(l[i])
        if op == '+':
            res += val
        else:
            res *= val
    return res


def part1():
    data = getPuzzle1()
    res = 0
    for op in data:
        res += calculate(op)
    return res


def getPuzzle2():
    data = []
    operations = []
    with open('input/day6.txt') as file:
        tmp = file.readlines()
        lines = np.array([list(l) for l in tmp[:-1]])
        lines = lines.transpose()[:-1]
        newline = True
        i = -1
        for line in lines:
            if all(x == ' ' for x in line):
                newline = True
                continue
            if newline:
                data.append([line])
                i += 1
                newline = False
            else:
                data[i].append(line)

        for val in tmp[-1]:
            if val == '+' or val == '*':
                operations.append(val)

    operations = operations[::-1]
    data = data[::-1]
    print(data[5])
    i = 0
    res = 0
    for col in data:
        tmp = -1
        for row in col[::-1]:
            word = ''
            for char in row:
                word += char if char != ' ' else ''

            print(f"{word}{operations[i]}", end='')
            if operations[i] == '*':
                if tmp == -1:
                    tmp = 1

                tmp *= int(word)

            else:
                if tmp == -1:
                    tmp = 0
                tmp += int(word)

        print(f"={tmp}")
        res += tmp
        i += 1
    return res


x = getPuzzle2()
print(x)
