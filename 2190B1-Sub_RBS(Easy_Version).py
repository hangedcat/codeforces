rep = int(input())

for _ in range(rep):
    n = int(input())
    s = input()
    
    total_open = s.count('(')
    seen_open = 0
    possible = False
    
    for i in range(n - 1):
        if s[i] == '(':
            seen_open += 1
        if s[i] == ')' and s[i+1] == '(':
            if total_open - seen_open - 1 > 0:
                possible = True
                break
    
    print(n - 2 if possible else -1)