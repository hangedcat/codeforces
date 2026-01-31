rep = int(input())

for _ in range(rep):
    n = int(input())
    s = input()
    u = set(s)
    ans = 0
    for i in u:
        ans += s.count(i) + 1
    print(ans)