def solution(P):
    result = 0
    firstRightArrowIdx = -1
    endLeftArrowIdx = -1
    for i in range(len(P)):
        if firstRightArrowIdx == -1 and P[i] == '>':
            firstRightArrowIdx = i
        if firstRightArrowIdx != -1 and P[i] == '<':
            endLeftArrowIdx = i
    if firstRightArrowIdx == -1 or endLeftArrowIdx == -1:
        return len(P)
    else:
        return len(P) - (endLeftArrowIdx - firstRightArrowIdx + 1)
print(solution("<<<><"))
print(solution("<<<<<<<<>>>"))
print(solution("<<><>><<><><<<>>"))