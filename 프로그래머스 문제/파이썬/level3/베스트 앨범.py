from collections import defaultdict
def solution(genres, plays):
    answer = []
    streaming = defaultdict(list)
    gen_rank = []
    for ix, (g, p) in enumerate(zip(genres, plays)):
        streaming[g].append((ix,p))
        streaming[g].sort(key = lambda x: x[1], reverse = True)
    
    for key in streaming:
        sum = 0
        for i in streaming[key]:
            sum += i[1]
        gen_rank.append((key,sum))
    
    gen_rank.sort(key = lambda x : x[1], reverse = True)

    # 수록
    for r in gen_rank:
        if len(streaming[r[0]]) == 1:
            answer.append(streaming[r[0]][0][0])
        else:
            for i, p in streaming[r[0]][:2]:
                answer.append(i)
    return answer
    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))