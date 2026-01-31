#this current version failed because it couldn't process bulk amount of data in short time
rep = int(input())

for _ in range(rep):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    

    for i in range(n):

        suffix_max = max(arr[i:n])

        if arr[i] < suffix_max:
            x = i
            y = arr.index(suffix_max, i, n)

            arr[x : y+1] = arr[x : y+1][::-1]
            break
    
    print(' '.join(map(str, arr)))