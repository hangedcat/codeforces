test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split(' '))
    arr_1 = list(map(int, input().split(' ')))
    arr_1.sort()
    arr_2 = list(map(int, input().split(' ')))
    arr_2.sort(reverse=True)

    total = 0
    for i in range(n):
        if i < m and arr_2[i] > arr_1[i]:
            total += arr_2[i]
        else:
            total += arr_1[i]

    print(total)