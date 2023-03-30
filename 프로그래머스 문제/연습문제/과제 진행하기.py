def solution(plans):
    answer = []
    # 시간을 전부 분으로 바꾸기
    for ix, p in enumerate(plans):
        name, time, studyingTime = p
        hour, minute = map(int, time.split(":"))
        time = 60 * hour + minute
        plans[ix][1] = time
        plans[ix][2] = int(studyingTime)
        
    # 시작 시간 순으로 정렬
    plans.sort(key = lambda x : x[1], reverse = True)
    stopAssignment = []
    curStudying = plans.pop()
    curTime = curStudying[1]
    # 잠시 멈춘 과제 Stack이나 Plan이 빌 떄까지 while문 지속
    while plans or stopAssignment:
        # 다음 거 뽑기
        nextStudying = plans.pop()
        # 현재 시간 + 현재 과제 완료까지 걸리는 시간이 다음 거 시작 시간보다 작을 때
        if curTime + curStudying[2] <= nextStudying[1]: # 현재 과제 완료
            answer.append(curStudying[0])
            curTime = curTime + curStudying[2]
            # 다음 과제가 시간 전까지 잠시 멈춘 과제가 있다면 계속 멈춘 과제 하기
            while stopAssignment:
                retry = stopAssignment.pop()
                if curTime + retry[2] <= nextStudying[1]:
                    answer.append(retry[0])
                    curTime = curTime + retry[2]
                else:
                    retry[2] = curTime + retry[2] - nextStudying[1]
                    stopAssignment.append(retry)
                    curTime = nextStudying[1]
                    curStudying = nextStudying
                    break
            else:
                curTime = nextStudying[1]
                curStudying = nextStudying
        else:
            curStudying[2] = curTime + curStudying[2] - nextStudying[1]
            stopAssignment.append(curStudying)
            curStudying = nextStudying
            curTime = nextStudying[1]
            
        if not plans:
            answer.append(curStudying[0])
            while stopAssignment:
                answer.append(stopAssignment.pop()[0])
            return answer
    
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))