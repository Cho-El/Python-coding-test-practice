def solution(call):
    array = {}
    delete = []
    s = set(call)
    for si in s:
        for c in call:
            if si == c or si == c.lower():
                if si in array:
                    array[si] += 1
                else:
                    array[si] = 1

    # 최대값 찾기
    delete = [k for k,v in array.items() if max(array.values()) == v]

    result = ''
    # 삭제 하고 남기기
    for c in call:
        if c not in delete and c.lower() not in delete:
            result += c

    return result


                

call = "ABCabcA"
print(solution(call))