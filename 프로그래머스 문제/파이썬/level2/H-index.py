def solution(citations):
    citations.sort()
    for ix, citation in enumerate(citations):
        if citation >= len(citations) - ix:
            return len(citations) - ix
    return 0



def solution2(citations):
    citations.sort()
    h = 0
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            h = i
        else:
            break
    return citations[h]

citations = [10,10,10,10,10]
print(solution(citations))
citations = [10,10,10,10,10]
print(solution2(citations))
