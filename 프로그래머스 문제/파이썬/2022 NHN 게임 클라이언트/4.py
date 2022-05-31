def dfs(players, depth, total_power, win_point, k):
    global answer
    if depth == len(players):
        answer = max(answer, total_power)
        return
    
    if players[depth] > total_power: # 질수 밖에 없는 경우
        dfs(players, depth + 1, total_power + k, 0, k)
    else:
        # 이기는 경우
        win_point += 1
        dfs(players, depth + 1, total_power + win_point, win_point, k)

        # 고의로 지는 경우
        dfs(players, depth + 1, total_power + k, 0, k)

def solution(players, power, k):
    global answer
    answer = 0
    dfs(players, 0, power, 0, k)
    return answer

if __name__ == '__main__':
    players = [[10, 11, 15, 14, 16, 18, 19, 20],[1, 2, 4, 7],[1, 2, 1, 2, 1]]
    power = [10,1,2]
    k = [2,2,100]
    for players, power, k in zip(players, power, k):
        print(solution(players, power, k))