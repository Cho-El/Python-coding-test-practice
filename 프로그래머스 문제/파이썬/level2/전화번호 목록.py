def solution(phone_book):
    answer = True
    hash = {}
    cnt = 0
    for i in phone_book:
        hash[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in hash and temp != i:
                answer = False
    
    return answer

print(solution(["119", "97674223", "1195524421"]))

