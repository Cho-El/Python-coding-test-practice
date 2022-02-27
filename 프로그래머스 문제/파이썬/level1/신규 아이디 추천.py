'''
    for id in new_id:
        if 'A'<= id <= 'Z': # 대문자
            id1 = chr(ord(id) - (ord('A') - ord('a')))
            new_id = new_id.replace(id, id1)
    '''
def solution(new_id):
    # Conter, replace, re.sub, join
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()


    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거합니다.
    for id in new_id:
        if 'a' <= id <= 'z' or '0' <= id <= '9' or id == '_' or id == '.' or id == '-': # id.isalpha() or c.isdigit()
            continue
        else :
            new_id = new_id.replace(id, '')

    # # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. 
    while('..' in new_id):
        new_id = new_id.replace('..','.')



    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id.strip('.')
    '''
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    '''
        
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not new_id :
        new_id = 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        new_id = new_id.rstrip('.')

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2 : 
        final_str = new_id[-1]
        while(len(new_id) < 3):
            new_id = new_id + final_str
    
    return new_id

new_id = "ge"
print(solution(new_id))


import re

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st









# from collections import Counter
# def solution(id_list, report, k):
# 	answer, check_list = [], []

# 	report_dict = {}

# 	for report_id in id_list :
# 		report_dict[report_id] = []

# 	for case in report:
# 		report_id, report_name = case.split()

# 		if report_name not in report_dict[report_id]:
# 			report_dict[report_id].append(report_name)
# 			check_list.append(report_name)

# 	cnt_dict = Counter(check_list)

# 	for report_id in id_list:
# 		answer.append(len([check for check in report_dict[report_id] if cnt_dict[check] >= k]))

# 	return answer