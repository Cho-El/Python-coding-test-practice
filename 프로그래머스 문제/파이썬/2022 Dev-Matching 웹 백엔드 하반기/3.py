def solution(k):
    global result_list
    # need = {
    #     '0' : 6,
    #     '1' : 2,
    #     '2' : 5,
    #     '3' : 5,
    #     '4' : 4,
    #     '5' : 5,
    #     '6' : 6,
    #     '7' : 3,
    #     '8' : 7,
    #     '9' : 6
    # }
    need = [6,2,5,5,4,5,6,3,7,6]
    result_list = []
    dfs(k, need, [])
    answer = len(result_list)
    print(result_list)
    return answer

def dfs(k,need, temp):
    global result_list
    if k == 0:
        if len(temp) != 1 and temp[0] == '0':
            return
        result_list.append(''.join(temp))
        return
    
    for i in range(len(need)):
        if k - need[i] >= 0 :
            temp.append(str(i))
            dfs(k - need[i], need, temp)
            temp.pop()
    return

print(solution(6))