rep = int(input())

for _ in range(rep):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    suffix_max = [0] * n
    suffix_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(arr[i], suffix_max[i+1])

    for i in range(n):
        if arr[i] == suffix_max[i]:
            continue


        target = suffix_max[i]
        j = i
        while arr[j] != target:
            j += 1

        arr[i:j+1] = arr[i:j+1][::-1]
        break

    print(' '.join(map(str, arr)))