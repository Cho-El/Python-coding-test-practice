import sys
sys.setrecursionlimit(10 ** 6)

# 1번 풀이
# def solution(queries):
#     answer = []
#     for n,p in queries:
#         target = splitBean(n, "Rr")
#         answer.append(target[p - 1])
#     return answer

# def splitBean(depth, parentString):
#     # depth가 1이면 바로 해당 스트링 리턴
#     if depth == 1:
#         return [parentString]
#     # 아닌 경우
#     else:
#         # 반씩 쪼개서 다시 호출
#         firstCase = parentString[0] * 2
#         midCase = parentString[0] + parentString[1]
#         lastCase = parentString[1] * 2
#         return splitBean(depth - 1, firstCase) + splitBean(depth - 1, midCase) + splitBean(depth - 1, midCase) + splitBean(depth - 1, lastCase)

# 2번 풀이

def 