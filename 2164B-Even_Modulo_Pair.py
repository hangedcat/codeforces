rep = int(input())

for _ in range(rep):
    length = int(input())
    seq = list(map(int, input().split()))
    
    found = False
    result = (-1, -1)
    
    for i in range(length):
        for j in range(i + 1, length):
            if (seq[j] % seq[i]) % 2 == 0:
                result = (seq[i], seq[j])
                found = True
                break
        if found:
            break
    
    if found:
        print(result[0], result[1])
    else:
        print(-1)
