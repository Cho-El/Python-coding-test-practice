from collections import defaultdict
def solution(clothes): # 조합
    closet = defaultdict(list)
    num_category = []
    answer = 1

    for name, category in clothes:
        closet[category].append(name)
    
    for key in closet.keys():
        num_category.append(len(closet[key]))
    
    for i in num_category:
        answer *= (i+1)
    
    answer -= 1

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))