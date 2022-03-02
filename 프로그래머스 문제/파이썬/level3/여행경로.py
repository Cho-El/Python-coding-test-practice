from collections import defaultdict

result = []

def dfs(n, start, tickets, answer):
    global result
    answer.append(start) # 출발점
    if n == len(tickets): # 모든 표를 다 돌아봤다면
        answer2 = answer[:]
        result.append(answer2)
        return True
    
    start_index = []
    for ix,(s,e,v) in enumerate(tickets):
        if not v and s == start: # 방문 체크 후 시작점이 start인 표 찾기
            start_index.append(ix)
    
    if not start_index: # start에 해당하는 표가 없다면
        return True

    for ix in start_index:
        tickets[ix][-1] = True
        if dfs(n+1 , tickets[ix][1], tickets, answer):
            tickets[ix][-1] = False
            answer.pop()
    
    return True



def solution(tickets) :
    global result
    for ticket in tickets: # 방문 확인을 위해
        ticket.append(False)
    answer =[]
    dfs(0, "ICN", tickets, answer)
    result.sort()
    return result[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

'''
그래프에서 뺏다가 아니면 다시 insert로 삽입
fp = footprint[:] 식의 deepcopy
'''
