rep = int(input())

for _ in range(rep):
    box = int(input())
    candies = list(map(int, input().split(' ')))
    lowest = min(candies)
    to_eat = []

    for i in range(box):
        if candies[i] == lowest:
            continue
        else:
            to_eat.append(candies[i] - lowest)

    print(sum(to_eat))