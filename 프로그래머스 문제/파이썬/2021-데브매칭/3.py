from collections import defaultdict
def dfs(seller, amount, parent):
    global answer
    if seller == 'center':
        return
    
    if amount // 10 < 1:
        answer[seller] += amount
        return
    else:
        interest = amount // 10
        answer[seller] += amount - interest
        dfs(parent[seller], interest, parent)
    
    return
    

def solution(enroll, referral, seller, amount):
    global answer
    parent  = {}
    answer = {}
    final_answer = []
    answer['center'] = 0
    for e, r in zip(enroll, referral):
        answer[e] = 0
        if r == '-':
            parent[e] = 'center'
            continue
        parent[e] = r
    
    for s, a in zip(seller, amount):
        dfs(s, a * 100, parent)

    for e in enroll:
        final_answer.append(answer[e])

    return final_answer

if __name__ == '__main__':
    enroll = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]]
    referral = [["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]]
    seller = [["young", "john", "tod", "emily", "mary"],["sam", "emily", "jaimie", "edward"]]
    amount = [[12, 4, 2, 5, 10],[2, 3, 5, 4]]
    for enroll, referral, seller, amount in zip(enroll, referral, seller, amount):
        print(solution(enroll, referral, seller, amount))