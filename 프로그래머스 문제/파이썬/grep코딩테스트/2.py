from itertools import combinations as com
import sys
INF = sys.maxsize

def cnt_pool(cb):
    for i in range(len(cb)-1):
        if cb[i] + 1 == cb[i+1]:
            return False
    return True

def solution(bricks, n, k):
    # graph = [[0 for _ in range(n)] for _ in range(len(bricks))] # 물이 0 벽돌이 1
    # for idx, brick in enumerate(bricks):
    #     for b in range(brick):
    #         graph[idx][b] = 1
    answer = INF
    temp = [i for i in range(1,len(bricks)-1)]
    
    for cb in com(temp, k-1):
        if cnt_pool(cb):
            add_brick = 0
            for idx in cb:
                add_brick += n - bricks[idx]
            answer = min(answer, add_brick)
    
    return answer

if __name__ == '__main__':
    bricks = [[1,2,5,3,1,0,2,3],[0, 1, 2, 3, 4],[0, 1, 2, 3, 4, 3]]
    n = [6,5,5]
    k = [3,2,2]
    for bricks, n, k in zip(bricks, n, k):
        print(solution(bricks, n, k))