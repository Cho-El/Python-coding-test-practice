def solution(record):
    answer = []
    result = []
    user_info = {}
    for r in record:
        sentence = list(r.split(' '))
        if len(sentence) == 3: # enter나 change일 때
            user_info[sentence[1]] = sentence[2]
            if sentence[0] == 'Change':
                continue
        answer.append(sentence)
    form = {
        'Enter':'님이 들어왔습니다.',
        'Leave':'님이 나갔습니다.'
    }
    for a in answer:
        if len(a) == 3: # enter인 경우
            a[2] = user_info[a[1]]


    return answer