def solution1(routes): # 내 풀이
    cnt = 0
    while routes:
        del_index = []
        a, b = routes.pop()
        a, b = min(a,b), max(a,b)
        for index, (c, d) in enumerate(routes):
            c,d = min(c,d), max(c,d)
            start = max(a,c)
            end = min(b,d)
            if end - start < 0:
                 continue
            else: # 겹치는 부분이 있다면
                del_index.append(index) # 겹치는 부분이 있는 차량의 index를 저장
                # 겹치는 부분이 다른 차량의 route와도 겹치는 검증
                a = start
                b = end
        for ix in reversed(del_index):
            del routes[ix]
        cnt += 1

    return cnt

def solution(routes):
    answer = 1
    routes = list(map(sorted,routes))
    routes.sort(key=lambda x:x[0], reverse=True)
    
    now = routes[0][0]
    for i in routes[1:]:
        if i[1] >= now:
            continue
        else:
            now = i[0]
            answer += 1
    
    return answer
routes = [[-5, -3], [15,-3]]
print(solution(routes))
