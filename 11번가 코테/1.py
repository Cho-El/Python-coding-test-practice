from collections import defaultdict
def solution(S):
    dict = {}
    result = 0
    # Implement your solution here
    for s in S:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] += 1
    
    for value in dict.values():
        if value % 2 != 0:
            result += 1
    
    return result

print(solution('acbcbba'))
print(solution('axxaxa'))
print(solution('aaaa'))