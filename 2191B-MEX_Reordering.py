t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    cnt0 = a.count(0)
    cnt1 = a.count(1)
    
    if cnt0 == 0:
        print("NO")
    elif cnt0 == 1:
        print("YES")
    else:  # cnt0 >= 2
        if cnt1 >= 1:
            print("YES")
        else:
            print("NO")