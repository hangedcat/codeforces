confirmed_column = []
confirmed_row = 0
for i in range(1, 6):
    line = input().split(' ')
    if '1' in line:
        confirmed_column.extend(line)
        confirmed_row = i

if confirmed_row != 3:
    x = abs(confirmed_row - 3)
else:
    x = 0

if (confirmed_column.index('1') + 1) != 3 :
    y = abs(confirmed_column.index('1') - 2)
else:
    y = 0

print(x + y)
