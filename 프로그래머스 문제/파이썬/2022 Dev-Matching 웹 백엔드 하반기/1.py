from atexit import register


def solution(registered_list, new_id):
    answer = ''
    check_list = {}
    for r in registered_list:
        check_list[r] = 1
    
    
    if not(new_id in check_list): # 없는 경우
        answer += new_id
        return answer
    else: # 아이디가 있는 경우
        while(True):
            newN = ''
            newS = new_id
            for i in range(len(new_id)):
                if new_id[i].isdigit():
                    newN = new_id[i:]
                    newS = new_id[:i]
                    break
            
            if not newN:
                newN = '1'
                new_id = newS + newN
            else:
                newN = str(int(newN) + 1)
                new_id = newS + newN
            
            if not (new_id in check_list):
                answer += new_id
                return answer