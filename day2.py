import math
data = []
with open('./day2.txt', 'r') as file:
    l = file.readline().strip()
    data = [(val.split('-')[0], val.split('-')[1]) for val in l.split(',')]


def divisori(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:       # If 'i' is a divisor of 'num'
            divisors.append(i)  # Add 'i' to the list of divisors
            if i != num // i:
                divisors.append(num // i)
    return divisors


def pattern(p, start, end, size):
    val = int(str(p)*size)
    print(f"p {p} val {val} end {end} size {size}")
    p = int(p)
    if end < val:
        return []
    if start > val:
        return [] + pattern(p+1, start, end, size)
    return [val] + pattern(p+1, start, end, size)


def genErrors(start, end):
    res = []
    if len(start) == 1 and len(end) == 1:
        return []

    while len(start) != len(end):
        start = '0'+start
    div = divisori(len(start))
    if len(div) == 0:
        return []
    for d in div:
        if d == len(start):
            continue
        p = pattern(start[:d], int(start), int(end), int(len(start)/d))
        res.append(p)
    return res


def run():
    pw = 0
    for (start, end) in data:
        print(f"start: {start}, end: {end}")
        err = genErrors(start, end)
        print(f"errors: {err}")
        for i in err:
            pw += int(i)
        print()

    print(pw)


run()
