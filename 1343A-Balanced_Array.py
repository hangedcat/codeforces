rep = int(input())
for _ in range(rep):
    n = int(input())
    if (n%4 != 0):
        print('NO')
        continue
    else:
        evens = list(range(2, n+1, 2))
        odds = list(range(1, n, 2))
        odds[-1] += n//2
        result = evens + odds
        print('YES')
        print(' '.join(map(str, result)))

