from bdb import Breakpoint


def solution(logs):
    answer = 0
    log_fig = ['team_name : ', ' application_name : ', ' error_level : ', ' message : ']
    for log in logs:
        if len(log) > 100:
            answer += 1
            continue
        
        cnt = 0
        # log형식에 맞는지 확인
        if log[0] == ' ':
            answer += 1
            continue

        for fi in range(len(log_fig)):
            if cnt != 0:
                break
            
            
            if fi != len(log_fig)-1 and log.find(log_fig[fi]) != -1: # 
                start = log.find(log_fig[fi]) + len(log_fig[fi])
                end = log.find(log_fig[fi + 1])
                value = log[start:end]
                for v in value:
                    if 'a' <= v <= 'z' or 'A' <= v <= 'Z':
                        continue
                    else:
                        cnt += 1
                        answer += 1
                        break
                
                if cnt != 0:
                    break
            
            elif fi == len(log_fig)-1 and log.find(log_fig[fi]) != -1:
                start = log.find(log_fig[fi]) + len(log_fig[fi])
                value = log[start:]
                for v in value:
                    if 'a' <= v <= 'z' or 'A' <= v <= 'Z':
                        continue
                    else:
                        cnt += 1
                        answer += 1
                        break

                if cnt != 0:
                    break

            else:
                answer += 1
                break
        
    return answer
            


logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
print(solution(logs))
