def solution(name, yearning, photo):
    answer = []
    score = {}
    for idx, n in enumerate(name):
        score[n] = yearning[idx]
    
    for p in photo:
        totalScore = 0
        for person in p:
            if person in score:
                totalScore += score[person]
        answer.append(totalScore)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))