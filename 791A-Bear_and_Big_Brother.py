weight = list(map(int, input().split(' ')))
year = 0
while weight[0] <= weight[1]:
    weight[0] *= 3
    weight[1] *= 2
    year += 1

print(year) 