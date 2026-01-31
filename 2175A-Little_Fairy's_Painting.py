rep: int = int(input())

for _ in range(rep):
    lenght = int(input())
    color = list(map(int, input().split(' ')))
    my_set = set(color)
    lenght2 = len(my_set)
    c = [x for x in my_set if x >= lenght2]

    
    print(min(c))


    