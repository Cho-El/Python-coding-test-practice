def solution(s):
    answer = 0
    startS = ""
    
    for ss in s:
        # 첫번째 문자가 비어 있는 경우 넣고 개수 세기
        if not startS:
            startS = ss
            numS = 1
            notSameNum = 0
            answer += 1
            continue
        # 비어 있지 않은 경우
        else:
            # 첫번째 문자랑 같은지 체크
            if startS == ss:
                # 같은 경우 횟수 증가
                numS += 1
            # 다른지 체크
            else:
                # 다른 경우 횟수 증가
                notSameNum += 1
                # 다른 경우 횟수가 같은 경우 횟수와 같은지 체크
                if notSameNum == numS:
                    # startS 초기화
                    startS = ''
    
    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
