def solution(routes):
	answer = 1
	routes.sort(key = lambda x: x[1])
	print(routes)
	camera = routes[0][1]
	for i in routes[1:]:
		if i[0] <= camera:
			continue
		else:
			camera = i[1]
			answer += 1
	return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))