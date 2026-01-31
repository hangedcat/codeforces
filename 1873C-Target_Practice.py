rep = int(input())

for _ in range(rep):
    score_dict = {}
    score = 0
    target: list[list] = []
    depth = 0
    negdepth = 9
    backdepth = 10
    for i in range(10):
        target.append(list(input()))

    for j in range(1, 6):
        score_dict[j] = 0
        if j < 5:
            for k in range(depth, backdepth):
                if target[depth][k] == 'X':
                    score_dict[j] += 1
            for k in range(depth, backdepth):
                if target[negdepth][k] == 'X':
                    score_dict[j] += 1
            for k in range(depth+1, backdepth-1):
                if target[k][depth] == 'X':
                    score_dict[j] += 1
            for k in range(depth+1, backdepth-1):
                if target[k][negdepth] == 'X':
                    score_dict[j] += 1
        else:
            for k in range(depth, backdepth):
                if target[depth][k] == 'X':
                    score_dict[j] += 1
            for k in range(depth, backdepth):
                if target[negdepth][k] == 'X':
                    score_dict[j] += 1
        
        depth += 1
        negdepth -= 1
        backdepth -= 1

    for key, value in score_dict.items():
        score += (key*value)
    
    print(score)