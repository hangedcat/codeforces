rep = int(input())

for _ in range(rep):
    n = int(input())
    a = list(map(int, input().split(' ')))

    x, y = a.count(1), a.count(2)
    if x == 1 and y == 1:
        print('NO')
        continue

    if ((x%2 == 0) and (y%2 == 0)) or ((x%2 == 0) and (x!=0) and (y%2 != 0)):
        print('YES')
        continue
    else:
        print('NO')

