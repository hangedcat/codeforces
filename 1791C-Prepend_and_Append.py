rep = int(input())

for i in range(rep):
    len_timur = int(input())
    timur = list(input())
    while True:
        if (len(timur) == 0) or (len(timur) == 1) or (timur[0] == timur[-1]):
            break
        else:
            timur.pop(0)
            timur.pop(-1)
    print(len(timur))
            


        
    

