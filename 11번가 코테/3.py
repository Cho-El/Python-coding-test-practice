# def solution(S):
#     result = 0
#     checkCors = 0
#     corFlag = 0
#     for s in S:
#         if s == '<':
#             if not corFlag:
#                 checkCors += 1
#             else:
#                 checkCors = 0
#                 corFlag = 0
#         else:
            
            
#     return result
from copy import deepcopy
def solution(S):
    global result
    result = 0
    dfs([], 0, 0, S, 0)
    return result

def dfs(stack, startIdx, flag, S, cnt):
    global result
    for i in range(startIdx,len(S)):
        # stack이 비어 있는 경우
        if not stack:
            if S[i] == '>':
                continue
            else:
                stack.append('<')
                result = max(result, cnt)
                flag = 0
                cnt = 0
        
        # stack이 차 있는 경우
        else:
            if flag == 0 and S[i] == '<':
                stack.append('<')
            elif flag == 1 and S[i] == '<':
                stack = []
                result = max(result, cnt)
                cnt = 0
            elif S[i] == '>':
                flag = 1
                stack.pop()
                cnt += 2
            else:
                # 물음표가 <인 경우
                copyStack = deepcopy(stack)
                stack.append('<')
                dfs(copyStack, i + 1, flag, S,cnt)
                stack.pop()
                # 물음표가 >인 경우
                copyStack = deepcopy(stack)
                flag = 1
                stack.pop()
                cnt += 2
                dfs(copyStack, i + 1, flag,S,cnt)
                

print(solution("<><??>>"))