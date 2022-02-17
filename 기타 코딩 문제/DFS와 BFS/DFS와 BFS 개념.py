'''
탐색 알고리즘: DFS/BFS
탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
'''
# 스택 자료구조------------------------------------------------
'''
스택 -> 선입후출의 자료 구조
'''
# 스택 구현
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

# 큐 자료구조-----------------------------------------------------
'''
큐 -> 선입선출의 자료구조
'''
# 큐 구현
from collections import deque

queue = deque() # 단순히 list로 구현 가능하지만 시간복잡도 면에서 deque를 사용하자.
# deque() -> 초기화는 list형태로 초기화할 수 있다. deque([1,2,3,4,5])
queue.append(5) # list append와 같다. 시간복잡도 O(1)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 가장 왼쪽에 있는 인자를 꺼낸다. 시간복잡도 O(1)
queue.append(1)
queue.append(4)
queue.popleft()
queue.pop() # 가장 오른쪽에 있는 인자를 꺼낸다.

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

# 재귀함수(Recursive Function)-------------------------------------
'''
재귀 함수란 자기 자신을 다시 호출하는 함수를 의미한다.
스택 형태로 돌아간다.
점화식

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.

재귀 함수의 형태

def 재귀함수:
	if 종료조건
	재귀함수()
	해당 재귀 함수가 수행할 코드

재귀 함수의 유의 사항
- 재귀 함수를 잘 활용 시 복잡한 알고리즘을 간결하게 작성할 수 있습니다.
=> 단 오히려 다른 사람이 이해하기 어려운 코드가 될 수 있으므로 신중하게 사용해야 한다.
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있습니다.
- 재귀 함수가 반복문보다 유리한 경우도 불리한 경우도 있습니다.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
=> 그래서 스택을 사용해야 할 떄 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니다.
'''
def recursive_function(i):
	# 20번째 호출을 했을 때 종료되도록 종료 조건 명시
	if i == 20 :
		return
	print(f'{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출합니다.')
	recursive_function(i+1)
	print(f'{i}번째 재귀함수를 종료합니다.')

recursive_function(1) 

# DFS(Depth-First Search)---------------------------------------------------------
'''
DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리를 한다.
방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
3. 더 이상 2번의 과정을 수행할 수 없을 떄까지 반복한다.

'''

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False]*9

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end = ' ')
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

dfs(graph,1,visited)
print()

# BFS(Breadth-First-Search) - 너비 우선 탐색----------------------------------------------------
'''
BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터
우선적으로 탐색하는 알고리즘이다.
- BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두
큐에 삽입하고 방문 처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
'''

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False]*9

def bfs(start,visited):
	queue = deque([start])
	visited[start] = True
	
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end = ' ')
		# 아직 방문하지 않은 인접한 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

bfs(1, visited)