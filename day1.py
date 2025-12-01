
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
    s = move[0]
    if s == 'R':
        passwd += int((cursor+n)/100)
        cursor = (cursor + n) % 100
    if s == 'L':
        passwd += int((cursor-n)/100)
        cursor = (cursor - n) % 100

    if precursor + y <= 0 or precursor + y > 99 or cursor == 0:
        passwd += 1
    if n >= 100:
        passwd += int((precursor+y)/100)
    print(f"move {move[0]} cursor {precursor} ({move[1]}) {
        cursor} \nHa passato lo zero {passwd - prepasswd} volte (tot: {passwd})\n")

    print(passwd)
