lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 19, 20, 40, 15, 25]
def solution():
    cnt = 0
    zero_cnt = 0
    lottos.sort()
    win_nums.sort()

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_cnt += 1
            continue
        else:
            for win in win_nums:
                if lottos[i] == win:
                    cnt += 1
                    continue
                if lottos[i] < win:
                    break

    best = cnt + zero_cnt
    worst = cnt
    if best > 6:
        best = 6
    if worst == 0:
        worst = 1
    if best == 0:
        best = 1

    return [7-best, 7-worst]

print(solution())

def solution2():
    cnt_0 = lottos.count(0)
    ans = 0
    for win in win_nums:
        if win in lottos:
            ans += 1
    
    rank = [6,6,5,4,3,2,1]
    return rank[cnt_0 + ans], rank[ans]

print(solution2())