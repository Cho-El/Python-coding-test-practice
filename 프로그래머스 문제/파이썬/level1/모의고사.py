answers = [1,3,2,4,2]
def solution():
    persons = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = [0,0,0]
    result2 = []
    for person in persons:
        for i in range(len(answers)):
            if answers[i] == person[i%len(person)]:
                result[persons.index(person)] += 1
    
    temp = max(result)
    for i in range(len(result)):
        if result[i] == temp:
            result2.append(i+1)
    return result2

# solution()

def solution2():
    persons = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = [0,0,0]
    result2 = []
    for ip, person in enumerate(persons):
        for i in range(len(answers)):
            if answers[i] == person[i%len(person)]:
                result[ip] += 1

    return [(i+1, v) for i, v in enumerate(result) if result[i] == max(result)]

print(solution2())