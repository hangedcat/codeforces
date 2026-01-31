n, t = map(int, input().split(' '))
queue = list(input())

for x in range(t):
    m = [i for i, x in enumerate(queue) if x=='B']
    for y in m:
        if y == (n-1):
            continue
        if queue[y+1] == 'G':
            queue[y] = 'G'
            queue[y+1] = 'B'
        
print(''.join(queue))           

