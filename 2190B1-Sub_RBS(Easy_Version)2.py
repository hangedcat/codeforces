rep = int(input())

for _ in range(rep):
    n = int(input())
    s = input()
    possible = False
    
    for i in range(n-1):
        if s[i] == '(':
            continue
        else:
            if s[i + 1] == '(':
                for j in range(i+2, n):
                    if s[j] == '(':
                        possible = True
                        break
                break
            else:
                continue
    print(n-2 if possible else -1)