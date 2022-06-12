import sys

def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)-1):
        min_ix = i
        for j in range(i+1,len(p)):
            if p[min_ix] > p[j]:
                min_ix = j
        
        if i != min_ix:
            p[min_ix], p[i] = p[i], p[min_ix]
            answer[i] += 1
            answer[min_ix] += 1
            
    return answer

if __name__ == '__main__':
    p = [[2,5,3,1,4], [2,3,4,5,6,1],[1,2,3,4,5,6,7,8,9]]

    for p in p:
        print(solution(p))
