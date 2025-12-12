def getPuzzleInput():
    with open('input/day7.txt') as file:
        return [list(line.strip()) for line in file.readlines()]


def countSplit(data, i, j):
    if i >= len(data) or j < 0 or j > len(data[i]) or data[i][j] == '|':
        return 0
    if data[i][j] == '^':
        return 1 + countSplit(data, i+1, j-1) + countSplit(data, i+1, j+1)
    data[i][j] = '|'
    return countSplit(data, i+1, j)


def part1():
    data = getPuzzleInput()
    j = 0
    for char in data[0]:
        if char == 'S':
            break
        j += 1
    print(2*countSplit(data, 1, j))


part1()
