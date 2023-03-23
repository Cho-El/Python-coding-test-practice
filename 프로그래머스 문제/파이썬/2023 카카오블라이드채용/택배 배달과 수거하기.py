# 오류 코드
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     while deliveries:
#         if deliveries[-1] == 0:
#             deliveries.pop()
#         else:
#             break
#     while pickups:
#         if pickups[-1] == 0:
#             pickups.pop()
#         else:
#             break

#     while deliveries or pickups:
#         distance = len(deliveries) if len(deliveries) > len(pickups) else len(pickups)
#         if deliveries:
#             deliveriesNum1 = deliveries.pop()
#             while deliveries and deliveriesNum1 <= cap:
#                 deliveriesNum2 = deliveries.pop()
#                 if deliveriesNum1 + deliveriesNum2 <= cap:
#                     deliveriesNum1 += deliveriesNum2
#                     continue
#                 else:
#                     deliveries.append(deliveriesNum2 - (cap - deliveriesNum1))
#                     break
        
#         if pickups:
#             pickupsNum1 = pickups.pop()
#             while pickups and pickupsNum1 <= cap:
#                 pickupsNum2 = pickups.pop()
#                 if pickupsNum1 + pickupsNum2 <= cap:
#                     pickupsNum1 += pickupsNum2
#                     continue
#                 else:
#                     pickups.append(pickupsNum2 - (cap - pickupsNum1))
#                     break
        
#         answer += 2 * distance

#     return answer


def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        deliveriesLength = 0
        pickupsLength = 0
        capD = cap
        capP = cap
        while deliveries:
            if deliveries[-1] == 0:
                deliveries.pop()
            else:
                deliveriesLength = len(deliveries)
                break
        while pickups:
            if pickups[-1] == 0:
                pickups.pop()
            else:
                pickupsLength = len(pickups)
                break
        while deliveries:
            num = deliveries.pop()
            capD -= num
            if capD >= 0:
                continue
            else:
                deliveries.append(abs(capD))
                break
        while pickups:
            num = pickups.pop()
            capP -= num
            if capP >= 0:
                continue
            else:
                pickups.append(abs(capP))
                break
        answer += 2 * max(deliveriesLength, pickupsLength)
            
    return answer
if __name__ == "__main__":
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
    print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
    print(solution(2,2,[0,0],[0,0]))
