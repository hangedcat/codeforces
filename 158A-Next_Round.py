x, y= map(int, input().split(' '))
score = list(map(int, input().split(' ')))

if score.count(0) != x:
    while score[y-1] == 0:
        score.pop(y-1)
        if y != 0 or x != 0:
            y -= 1
            x -= 1

if score[0] == 0:
    y = 0
else:   
    for _ in range(x-y):
        if score[y-1] == score[y]:
            y += 1
        else:
            break
        
print(y)



