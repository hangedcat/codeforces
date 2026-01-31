n = int(input())
a = 0
for _ in range(n):
    num = input()
    list_num = num.split(" ")
    if list_num.count('1') > 1:
        a += 1
    else:
        continue
print(a)