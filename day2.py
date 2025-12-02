data = []
with open('./day2.txt', 'r') as file:
    l = file.readline().strip()
    data = [(val.split('-')[0], val.split('-')[1]) for val in l.split(',')]


def check(val, i, j):
    if j >= len(val):
        return True
    return val[i] == val[j] and check(val, i+1, j+1)


def eval(val):
    if len(val) % 2 == 0:
        return check(val, 0, int(len(val)/2))
    return check(val, 0, int(len(val)/2)-1)


def rg():
    pw = 0
    for val in data:
        start, end = val
        for n in range(int(start), int(end)):
            if len(str(n)) == 1:
                continue
            if not eval(str(n)):
                pw += n
    print(pw)


rg()
