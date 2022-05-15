from collections import deque
def solution(n, text, second):
    answer = deque(['_' for _ in range(n)])
    q1 = deque(['_' for _ in range(n)])
    while second != 0:
        # text 다돌기
        for t in text:
            second -= 1
            answer.popleft()
            if t == ' ':
                answer.append('_')
            else:
                answer.append(t)

            # second가 0이 되었다면 break
            if second == 0:
                break
        else:
            # text를 다 돌았다면 '_'를 추가하기
            for _ in range(n):
                second -= 1
                answer.popleft()
                answer.append('_')
                if second == 0:
                    break
    
    answer = ''.join(answer)
    return answer

if __name__ == '__main__':
    n = [6,6,6]
    text = ['hi bye','hi bye','hi bye']
    second = [1,2,6]
    for n, text, second in zip(n,text,second):
        print(solution(n,text,second))