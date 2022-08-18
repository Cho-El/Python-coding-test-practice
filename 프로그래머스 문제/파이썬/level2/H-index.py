from re import L


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

def solution3(citations):
    citations.sort()
    h_idx = 0
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            h_idx = i
        else:
            break
    return citations[h_idx]

def solution4(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count - i
    return 0

citations = [0,1,3,3,3,4,4,4,6,7]
print(solution4(citations))
print(solution3(citations))
citations = [10,10,10,10,10]
print(solution4(citations))
print(solution3(citations))
citations = [0,0,0,0,1]
print(solution4(citations))
print(solution3(citations))

citations = [3,0,6,1,5,9]
print(solution4(citations))
print(solution3(citations))
