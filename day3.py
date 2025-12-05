data = []
with open('./day3.txt', 'r') as file:
    data = [list(map(int, val.strip())) for val in file.readlines()]


# coontrollo che n faccia parte di una configurazione di val > a vals
# in tal caso ritorno la configurazione di val maggiore
def check(vals, n):
    res = vals
    for i in range(len(vals)):
        # stringa senza il val i-esimo e con n in coda
        val = vals[:i] + vals[i+1:]+str(n)
        if (int(val) > int(res)):
            res = val
    return res


def joltage(size):
    res = 0
    for row in data:
        vals = ''
        # creo una stringa di dimensione size iniziale (a cui aggiungero'/togliero' valori)
        for i in range(size):
            vals += str(row[i])

        for i in range(len(vals), len(row)):
            vals = check(vals, row[i])
        res += int(vals)
    return res


print(joltage(12))
