def getPuzzleInput():
    with open('input/day7.1.txt') as file:
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
    print(countSplit(data, 1, j))


def countSplit2(data, i, j):
    # se sono fuori dalla tabella o
    # ho trovato un percorso gia' percorso da qualcuno (caso '|')
    if i >= len(data):
        return 1
    if j < 0 or j > len(data[i]) or data[i][j] == '|':
        return 0
    if data[i][j] == '^':
        return (countSplit2(data, i+1, j-1) + countSplit2(data, i+1, j+1))
    data[i][j] = '|'
    return 2*countSplit2(data, i+1, j)


def part2():
    data = getPuzzleInput()
    j = 0
    for char in data[0]:
        if char == 'S':
            break
        j += 1
    print(countSplit2(data, 1, j))


part1()
part2()
