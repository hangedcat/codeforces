import numpy as np
rep = int(input())

for _ in range(rep):
    score_dict = {}
    score = 0
    target: list[list] = []
    depth = 0
    backdepth = 10
    for i in range(10):
        target.append(list(input()))

    target_arr = np.array(target)

    for j in range(1, 6):
        score_dict[j] = 0
        if j < 5 :
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[depth , depth:backdepth] == 'X')
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[depth+1:backdepth-1 , depth] == 'X')
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[-j , depth:backdepth] == 'X')
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[depth+1:backdepth-1 , -j] == 'X')
            depth += 1
            backdepth -= 1
        else:
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[depth , depth:backdepth] == 'X')
            score_dict[j] = score_dict[j] + np.count_nonzero(target_arr[j , depth:backdepth] == 'X')
        
    print(sum(score_dict.values()))