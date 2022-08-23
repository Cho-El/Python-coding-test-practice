# def solution1(record):
#     answer = []
#     result = []
#     user_info = {}
#     for r in record:
#         sentence = list(r.split(' '))
#         if len(sentence) == 3: # enter나 change일 때
#             user_info[sentence[1]] = sentence[2]
#             if sentence[0] == 'Change':
#                 continue
#         answer.append(sentence)
   
#     for a in answer:
#         if a[0] == 'Enter': # enter인 경우
#             a[2] = user_info[a[1]]
#             temp_str = a[2] + '님이 들어왔습니다.'
#             result.append(temp_str)
#         else:
#             temp_str = user_info[a[1]] + '님이 나갔습니다.'
#             result.append(temp_str)

#     return result

def solution(record):
    user_info = {}
    temp = []
    result = []
    for r in record:
        info = r.split()
        if len(info) == 3: # enter 또는 change
            user_info[info[1]] = info[2]
            if info[0] == "Enter":
                temp.append([info[1], "님이 들어왔습니다."])
        else: # Leave
            temp.append([info[1],"님이 나갔습니다."])
    
    for t in temp:
        t[0] = user_info[t[0]]
        result.append(''.join(t))
    
    return result
if __name__ == '__main__':
    i = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(i))