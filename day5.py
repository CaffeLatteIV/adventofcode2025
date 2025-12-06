intervals = []
data = []
with open('input/day5.txt') as file:
    switch = False
    for line in file.readlines():
        if len(line) == 0 or line == '' or line == '\n':
            switch = True
        elif not switch:
            vals = line.strip().split('-')
            intervals.append(
                (int(vals[0]), int(vals[1])))
        else:
            data.append(int(line))


def spoiled(n, l):
    for (start, end) in l:
        if n >= start and n <= end:
            return False
    return True


def part1():
    res = 0
    for n in data:
        if not spoiled(n, intervals):
            res += 1
    return res


def cleanIntervals(l):
    blist = [l[0]]
    for (start, end) in l:
        add = True
        for i in range(len(blist)):
            # bs = 10 be = 20
            bs, be = blist[i]
            # case start = 9, end = 11
            if start <= bs and end >= bs and end <= be:
                bs = start
                add = False
            elif start <= bs and end >= be:
                bs = start
                be = end
                add = False
            elif start >= bs and start <= be and end >= be:
                add = False
                be = end
            elif start >= bs and end <= be:
                add = False
                continue
            blist[i] = (bs, be)
        if add:
            blist.append((start, end))

    return blist


def clean():
    print("Generating first clean interval")
    blist = cleanIntervals(intervals)
    cont = True
    print(f"Cleaning blist (len: {len(blist)})")
    while cont:
        nblist = cleanIntervals(blist)
        if len(nblist) == len(blist):
            cont = False
        blist = nblist
    return blist


def count():
    summ = 0
    blist = clean()
    for (start, end) in blist:
        summ += end-start+1
    return summ


print("Result")
print(count())
