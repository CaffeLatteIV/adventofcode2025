data = []
with open('./day3.txt', 'r') as file:
    data = [list(map(int, val.strip())) for val in file.readlines()]


def check(vals, n):
    res = vals
    for i in range(len(vals)):
        val = vals[:i] + vals[i+1:]+str(n)
        if (int(val) > int(res)):
            res = val
    return res


def joltage(size):
    res = 0
    for row in data:
        vals = ''
        for i in range(size):
            vals += str(row[i])

        for i in range(len(vals), len(row)):
            vals = check(vals, row[i])
        res += int(vals)
        print(row)
        print(vals)
        print()
    print(res)


joltage(12)
