rep = int(input())

for _ in range(rep):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a[a.index(min(a))] += 1
    product = 1
    for i in a:
        product *= i

    print(product)

