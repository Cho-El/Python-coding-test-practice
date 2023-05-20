from collections import defaultdict
def closestStraightCity(c, x, y, q):
    result = []
    # Write your code here
    dictX = defaultdict(list)
    dictY = defaultdict(list)
    dictCityName = {}
    
    # 이름 좌표 저장, x 공동 구역, y 공동 구역 따로 저장
    for cityName, x, y in zip(c,x,y):
        dictCityName[cityName] = [x,y]
        dictX[x].append((cityName, y))
        dictY[y].append((cityName, x))
    
    # 딕셔너리 안에 값 정렬하기
    for i in dictX:
        dictX[i].sort(key = lambda x : x[1])
    for i in dictY:
        dictY[i].sort(key = lambda x : x[1])
        
    for cityName in q:
        qx, qy = dictCityName[cityName]
        nearestCity = []
        # x 공동 구역 체크
        for idx, info in enumerate(dictX[qx]):
            if cityName == info[0]:
                # 찾은 도시 앞 인덱스
                if idx - 1 >= 0:
                    nearestCity.append([dictX[qx][idx - 1][0], abs(dictX[qx][idx - 1][1] - qy)])
                # 찾은 도시 뒤 인덱스
                if idx + 1 < len(dictX[qx]):
                    nearestCity.append([dictX[qx][idx + 1][0], abs(dictX[qx][idx + 1][1] - qy)])
        # y 공동 구역 체크
        for idx, info in enumerate(dictY[qy]):
            if cityName == info[0]:
                if idx - 1 >= 0:
                    nearestCity.append([dictY[qy][idx - 1][0], abs(dictY[qy][idx - 1][1] - qx)])
                if idx + 1 < len(dictY[qy]):
                    nearestCity.append([dictY[qy][idx + 1][0], abs(dictY[qy][idx + 1][1] - qx)])
        # 공동 구역이 없는 경우
        if not nearestCity:
            result.append("NONE")
        # 있는 경우
        else:
            nearestCity.sort(key = lambda x : [x[1],x[0]])
            result.append(nearestCity[0][0])
    
    return result

print(closestStraightCity(['london','warsaw','hackerland'],[1,10,20],[1,10,10],['london','warsaw','hackerland']))