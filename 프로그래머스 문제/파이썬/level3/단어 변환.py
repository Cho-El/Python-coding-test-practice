from collections import deque

def bfs(begin, target, words):

    visited = [False] * len(words)
    how_many = 0
    q = deque([(begin,0)])

    while q:
        now, depth = q.popleft() # 현재 비교 대상
        if now == target: # 현재 비교 대상과 타겟값이 같은 경우
            return depth

        # begin과 한 단어만 다른 경우
        for ix, word in enumerate(words): # 단어들을 돌면서 한 개만 다른 경우 탐색
            cnt = 0
            if visited[ix] :
                continue
            for n,w in zip(now, word):
                if cnt >= 2: # 다른 글자가 두개 이상인 경우
                    break
                if n != w: # 글자가 다른 경우 
                    cnt += 1
            if cnt == 1: # 한개만 다른 것들
                visited[ix] = True
                q.append((word, depth + 1))
    
    return 0


def solution(begin, target, words):
    if target in words:
        return bfs(begin, target, words)
    else:
        return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))