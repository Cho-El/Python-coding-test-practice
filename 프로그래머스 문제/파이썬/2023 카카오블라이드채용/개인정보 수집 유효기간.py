def solution(today, terms, privacies):
    answer = []
    monthList = [12,1,2,3,4,5,6,7,8,9,10,11]
    termsDict = {}
    for t in terms:
        termName, period = t.split()
        termsDict[termName] = int(period)
    
    today = list(map(int,today.split('.')))
    for idx, p in enumerate(privacies, 1):
        privacyDate, privacyName = p.split()
        privacyDate = list(map(int, privacyDate.split('.')))
        addMonth = privacyDate[1] + termsDict[privacyName]
        if addMonth % 12  == 0:
            privacyDate[0] += addMonth // 12 - 1
        else:
            privacyDate[0] += addMonth // 12
        privacyDate[1] = monthList[addMonth % 12]

        if today >= privacyDate:
            answer.append(idx)

    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))