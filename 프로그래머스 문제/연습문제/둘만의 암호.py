def solution(s, skip, index):
    answer = ''
    alphabet = ''
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in skip:
            alphabet += chr(i)
    
    for i in s:
        startIdx = alphabet.find(i)
        startIdx += index
        startIdx %= len(alphabet)
        answer += alphabet[startIdx]
    
    return answer

print(solution('aukks','wbqd',5))