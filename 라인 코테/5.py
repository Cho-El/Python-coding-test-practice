def solution(abilities,k):

	abilities.sort(reverse = True)
	rival = [0 for _ in range((len(abilities)+1) // 2)]
	me = [0 for _ in range((len(abilities)+1) // 2)]

	for i in range(len(abilities)):
		if i % 2 == 0:
			rival[i//2] += abilities[i]
		else:
			me[i//2] += abilities[i]
	
	dif = []
	for ix, (r,m) in enumerate(zip(rival, me)):
		temp = r-m
		dif.append([temp,ix])
	
	dif.sort(reverse = True, key = lambda x:x[0])
	for i in range(k):
		rival[dif[i][1]], me[dif[i][1]] = me[dif[i][1]], rival[dif[i][1]]
	
	return sum(me)


k = 1
abilities1 = [7,6,8,9,10]
k = 2
abilities = [2,8,3,6,1,9,1,9]
print(solution(abilities1,1))