
data = []
with open('./day1.txt', 'r') as file:
    data = [(line.strip()[0], line.strip()[1:]) for line in file]

passwd = 0
cursor = 50
for move in data:
    precursor = cursor
    prepasswd = passwd
    n = int(move[1])
    y = -int(move[1]) if move[0] == 'L' else int(move[1])
    c = n % (int(n/100)*100) if n >= 100 else n
    s = move[0]
    if s == 'R':
        passwd = passwd+1 if cursor + c > 100 and cursor != 0 else passwd
        cursor = (cursor + c) % 100
    if s == 'L':
        passwd = passwd+1 if cursor - c < 0 and cursor != 0 else passwd
        cursor = (cursor - c) % 100

    if cursor == 0:
        passwd += 1
    if n >= 100:
        passwd += int(n/100)

    if prepasswd < passwd:
        print(f"move {move[0]} cursor {precursor} ({move[1]}) {
            cursor} \nHa passato lo zero {passwd - prepasswd} volte (tot: {passwd})\n")

print(passwd)
