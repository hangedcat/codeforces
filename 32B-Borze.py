ternary = list(input())
x = 0
y = len(ternary)
borze = []

while x < y:
    if ternary[x] == '.':
        borze.append('0')
        x += 1
    else:
        if ternary[x + 1] == '.':
            borze.append('1')
            x += 2
        else:
            borze.append('2')
            x += 2

print(''.join(borze))
