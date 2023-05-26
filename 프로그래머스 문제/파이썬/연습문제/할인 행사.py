def solution(want, number, discount):
    answer = 0
    # 딕셔너리 만들기
    info = {}
    for w,n in zip(want,number):
        info[w] = n
    sumNum = sum(number)
    
    # 10개씩 검사
    for i in range(len(discount) - sumNum + 1):
        # 첫번째 검사일떄
        if i == 0:
            for d in discount[i : i + sumNum]:
                if d in info:
                    info[d] -= 1
            
        # 그 밖에 검사일 때
        else:
            prev = discount[i - 1]
            nextD = discount[i + sumNum - 1]
            if prev in info:
                info[prev] += 1
            if nextD in info:
                info[nextD] -= 1
        
        if allDiscount(info):
            answer += 1
            
    return answer

def allDiscount(target):
    for v in target.values():
        if v > 0:
            return False
    return True