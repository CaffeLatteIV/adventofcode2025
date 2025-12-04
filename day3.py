data = []
with open('./day3.txt', 'r') as file:
    data = [list(map(int, val.strip())) for val in file.readlines()]


res = 0
for row in data:
    m = 0
    pre = 0
    index = 0
    for i in range(len(row)):
        if row[i] > m:
            m = row[i]
            index = i
    for i in range(index+1, len(row)):

    print(row)
    print(f"m {m} pre {pre}")
    print()
    res += int(str(pre) + str(m))

print(res)
