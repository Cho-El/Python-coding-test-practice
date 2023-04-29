def solution(originals, fakes):
    listOriginals = []
    listFakes = []
    answer = []
    for origin in originals:
        origin = origin.upper()
        setDict = set()
        for s in origin.split():
            setDict.add(s)
        listOriginals.append(setDict)
    
    for fake in fakes:
        fake = fake.upper()
        setDict = set()
        for s in fake.split():
            setDict.add(s)
        listFakes.append(setDict)
    
    for fake in listFakes:
        isFake = 0
        for origin in listOriginals:
            if len(fake) == len(origin):
                isFake = 1
                for s in fake:
                    if s not in origin:
                        isFake = 0
                        break

                if isFake:
                    break
        if isFake:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

print(solution(["A B C D E", "F G"], ["A b C d E", "E D C B A", "F G G G G", "A B C D E"]))
print(solution(["A A b C", "X Y Z", "A X Y"], ["A A b C X Y Z", "A B C X", "A C B C B", "Q", "A A b"]))