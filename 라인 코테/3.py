def solution(n, remote, office, employ):
	group = [[]] + [[] for _ in range(n)]
	possible = []

	for ie, e in enumerate(employ):
		value = list(e.split(' '))
		group[int(value[0])].append(ie+1)

		check = True
		for i in value[1:]:
			if i not in remote:
				check = False
				break
		
		if check:
			possible.append(ie+1)
		
	possible.sort(reverse = True)
	for i in possible:
		cnt = 0
		for j in range(1,len(group)):
			if i in group[j] and len(group[j]) > 1:
				group[j].pop(group[j].index(i))
				cnt += 1
		
		if not cnt:
			possible.pop(possible.index(i))

	possible.sort()

	return possible

num_teams = 3
remote_tasks = ['development','marketing','hometask'] # 재택 가능한 업무
office_tasks = ['recruitment', 'education', 'officetask']
employees = ['1 development hometask', '1 recruitment marketing','2 hometask','2 development marketing hometask', '3 marketing', '3 officetask', '3 development']

num_teams1 = 2
remote_tasks1 = ['design'] # 재택 가능한 업무
office_tasks1 = ['building','supervise']
employees1 = ['2 design', '1 supervise building design','1 design','2 design']

print(solution(num_teams, remote_tasks, office_tasks, employees))
print(solution(num_teams1, remote_tasks1, office_tasks1, employees1))
