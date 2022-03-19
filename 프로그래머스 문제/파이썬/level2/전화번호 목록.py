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

def solution2(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

print(solution2(["12","123","1235","567","88"]))

