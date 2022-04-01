import sys
from bisect import bisect_left
from bisect import bisect_right
# 888999777112200666646468787
# s = list(sys.stdin.readline().rstrip())

def solution(s):
    s = list(s)
    s.sort()
    s_sets = set(s)
    s_num = []
    even = [] # 문자열안 숫자가 짝수개인것 저장
    odd = [] # 문자열안 숫자가 홀수개인것 저장

    # 각 숫자와 그 숫자의 갯수를 저장
    for i in s_sets: 
        l = bisect_left(s, i)
        r = bisect_right(s, i)
        dis = r-l
        s_num.append((i,dis))
    # 숫자의 크기 순으로 정렬
    s_num.sort(reverse = True, key = lambda x : x[0])

    '''
    어차피 펠린드롬수는 각 숫자의 개수가 짝수인 것들로만 이루어지던가 ex) 5544224455 -> 5가 4개 4가 4개 2가 2개 -> 각 숫자의 갯수가 모두 짝수
    아니면 각 숫자의 개수가 짝수인 것과 홀수인 것 1개로만 이루어질 수 있다. ex) 55544144555 -> 5가 6개, 4가 4개, 1이 1개 -> 1의 갯수만 홀수

    1. 큰 수가 나오려면 길이가 최대여야 하므로 개수가 짝수인 것은 모두 포함
    2. 홀수개의 숫자가 있다면 그 중에 가장 큰 값을 포함
    '''
    for i in s_num:
        if i[1] % 2 == 0: # 해당 숫자의 갯수가 짝수일 때
            even.append(i)
        else:
            odd.append(i) # 해당 숫자의 갯수가 홀수일 때
            odd.sort(reverse = True, key = lambda x : x[1])  
    
    if odd: # 홀수개의 숫자를 가지고 있다면
        even.append(odd[0])
    even.sort(reverse = True, key = lambda x : x[0])

    temp = ''
    # 절반만 구함
    for e in even:
        temp += e[0] * (e[1]//2)
        if e[1]%2 == 1:
            mid = e[0]
    
    if odd:
        temp += mid
        if temp[0] == '0':
            result = mid
        else:
            result = temp + ''.join(list(reversed(temp))[1:])
    else:
        if temp[0] == '0':
            result = 0
        else:
            result = temp + temp

    # print(int(result))
    return result

def solution2(S):
    arr = [0] * 10
    while S:
        t = int(S[-1])
        S = S[:-1]
        arr[t] += 1

    start = ""
    middle = ""
    for i in range(9, -1, -1):
        while arr[i] >= 2:
            if i == 0:
                if len(start) == 0:
                    arr[i] = 1
                    continue

            start = start + str(i)
            arr[i] -= 2
        if arr[i] >= 1 and middle == "":
            middle = str(i)
    return start + middle + start[::-1]


if __name__ == "__main__":
    print(solution("39878"),solution2("39878"))
    print(solution("00900"),solution2("00900"))
    print(solution("0000"),solution2("0000"))
    print(solution("54321"),solution2("54321"))
    print(solution("54405"),solution2("54405"))
    print(solution("544305"),solution2("544305"))
    print(solution("505"),solution2("505"))
    print(solution("10005"),solution2("10005"))
