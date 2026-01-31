rep = int(input())

for _ in range(rep):
    l = int(input())
    arr = list(map(int, input().split(' ')))
    even = 0
    odd = 0
    for i in range(l):
        if i % 2 == 0:
            if arr[i] % 2 != 0:
                even += 1
        else:
            if arr[i] % 2 == 0:
                odd += 1
    if even == odd:
        print(even)
    else:
        print(-1)
