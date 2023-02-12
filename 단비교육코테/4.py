
def solution(play_list,listen_time):
    lenList = len(play_list)
    new_play_list = 2 * play_list # 뒤에서 앞으로 가는 곡들을 세기 위해서
    end = 0
    sumTime = 0
    result = 0
    # 시작점 설정 시작점은 play_list의 마지막 원소 전까지만
    for start in range(lenList):
        # 끝점은 new_play_list 끝까지, 
        while end < len(new_play_list):
            # end값이 시작지점이라면 sumTime에 1을 더해주고 end 증가
            if start == end:
                sumTime += 1
                end += 1
                continue
            # end - start가 이미 play_list 길이를 넘는 경우 최대값이므로 return하고 종료
            if end - start >= lenList:
                return lenList
            
            # sumTime이 listen_time보다 작을 때 sumTime에 리스트에 end값 더해주기, end 증가
            if sumTime < listen_time:
                sumTime += new_play_list[end]
                end += 1
                
            # sumTime이 listen_time보다 같거나 클 때, result 업데이트, while 문 종료
            else:
                result = max(result, end - start)
                break
        sumTime -= new_play_list[start + 1]
        
    return result

if __name__ == "__main__":
    play_list = [[1,2,3,4],[2,3,1,4],[1,2,3,4]]
    listen_time = [5,3,20]
    for a, b in zip(play_list, listen_time):
        print(solution(a,b))
