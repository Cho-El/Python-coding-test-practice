def solution(sentences, n):
    score = [0 for _ in range(16)]
    need_key = [[] for _ in range(16)]
    result = []

    for ix, sentence in enumerate(sentences):
        for i in sentence:
            # 점수구하기
            if i.isupper():
                score[ix] += 2
            else:
                score[ix] += 1
            if i == ' ':
                continue

            # 필요한 키 구하기
            if i.isupper() and i.lower() not in need_key[ix]:
                need_key[ix].append(i.lower())
                if '!' not in need_key[ix]:
                    need_key[ix].append('!')
            
            elif i not in need_key[ix]:
                need_key[ix].append(i)

        need_key[ix].sort()
    # for i in range(len(need_key)):
    #     print(need_key[i],score[i], end = ' ')
    # print()

    union1 = []
    for i in range(len(need_key)-1):
        for j in range(i+1, len(need_key)):
            temp = set(need_key[i])|set(need_key[j])
            if len(temp) <= n and temp not in union1:
                union1.append(temp)

    for ix,i in enumerate(union1):
        score_sum = 0
        for ij,j in enumerate(need_key):
            temp = i&set(j)
            if temp == set(j):
                score_sum += score[ij]
        union1[ix] = score_sum
    
    return max(union1)

sentences = ["ABcD", "bdbc", "a", "Line neWs"]
sentences = ["line in line", "LINE", "in lion"]
n = 5
print(solution(sentences, n))