def solution(e, starts):
    num = [0 for _ in range(e+1)]

    # end까지 개수 저장하기
    for i in range(1, e+1):
        for j in range(i, e+1):
            idx = i * j
            # j * k가 e보다 크다면 break
            if idx > e:
                break
            # 숫자가 동일한 경우 1 증가
            if i == j:
                num[idx]
            # 숫자가 다른 경우 2 증가
            else:
                num[idx] = num[idx] + 2

    result = [0] * (e+1)
    max_value = 0

    for i in range(e, 0, -1):
        if num[i] >= max_value:
            max_value = num[i]
            result[i] = i
        else:
            result[i] = result[i + 1]

    return [result[start] for start in starts]