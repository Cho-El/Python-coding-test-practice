# def solution(id_list, report, k):
# 	report_dict = {id_: set() for id_ in id_list}
# 	for each in report:
# 		user_id, report_id = each.split(' ')
# 		report_dict[report_id].add(user_id)
# 	answer = {id_: 0 for id_ in id_list}
# 	for key, values in report_dict.items():
# 		if len(values) >= k:
# 			for value in values:
# 				answer[value] += 1
# 	return list(answer.values())


# def solution(id_list, report, k):
#     declare = {} # 신고당한 사람 : 신고한 사람
#     declared = [] # 유저 순서대로 신고 당한 수
#     answer = {}
#     for i in id_list: # 유저 수 만큼 배열 생성
#         declare[i] = []
#         answer[i] = 0

#     for i in report:
#         a, b = i.split(" ") # 신고하는 사람과 당한 사람을 나눔
#         if a not in declare[b]: # 중복 신고 체크
#             declare[b].append(a) # 중복이 아니라면 추가

#     for i in declare.values(): # 각 유저별 신고 당한 수 저장
#         declared.append(len(i))

#     for index, value in enumerate(declared): # 인덱스와 값을 돌림
#         if value >= k: # k번 이상 신고 당했을 때
#             for i in declare[id_list[index]]: # 신고한 사람에게 +1씩
#                 answer[i] += 1

#     return list(answer.values()) # 신고한 사람이 받은 메일

from collections import Counter
def solution(id_list, report, k):
	answer, check_list = [], []

	report_dict = {}

	for report_id in id_list :
		report_dict[report_id] = []

	for case in report:
		report_id, report_name = case.split()

		if report_name not in report_dict[report_id]:
			report_dict[report_id].append(report_name)
			check_list.append(report_name)

	cnt_dict = Counter(check_list)

	for report_id in id_list:
		answer.append(len([check for check in report_dict[report_id] if cnt_dict[check] >= k]))

	return answer