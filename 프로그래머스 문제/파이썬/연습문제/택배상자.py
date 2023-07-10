from collections import deque
def solution(order):
    result = 0
    startNum = 1
    sub = []
    for o in order:
        while startNum <= len(order) or sub:
            # order에 있는 숫자 main에 있는 숫자인지 체크
            if startNum == o:
                result += 1
                startNum += 1
                break
            # 같지 않은 경우
            else:
                # startNum이 o보다 큰 경우 -> 이미 sub에 들어가 있음
                if startNum > o :
                    # sub에 값이 있는 경우 마지막 값 비교
                    if sub and sub[-1] == o:
                        sub.pop()
                        result += 1
                        break
                    else:
                        return result
                # 작은 경우 startNum을 sub에 넣고 다음 상자를 확인
                else:
                    sub.append(startNum)
                    startNum += 1
                    
    return result
    
# 4 3 1 2 5
# 1 2 3 보조 컨테이너
# 4 3
