def solution(participant, completion):
	hashDict = {}
	sumHash = 0
	
	# 참가자 dictionary 만들기
	# 참가자의 sum(hash) 구하기
	for part in participant:
		hashDict[hash(part)] = part
		sumHash += hash(part)
	
	for comp in completion:
		sumHash -= hash(comp)
	
	return hashDict[sumHash]