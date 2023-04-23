def solution(s):
    answer = []
    dict = {}
    for idx, string in enumerate(s):
        if string not in dict:
            dict[string] = dict.get(string,idx)
            answer.append(-1)
        else:
            answer.append(idx - dict[string])
            dict[string] = idx
    return answer