def solution(sequence):
    answer = 0
    pulseSeqNum1 = 1
    pulseSeqNum2 = -1
    newS1 = []
    newS2 = []
    for s in sequence:
        newS1.append(s * pulseSeqNum1)
        newS2.append(s * pulseSeqNum2)
        pulseSeqNum1 *= -1
        pulseSeqNum2 *= -1
    
    dp1 = [0] * len(sequence)
    dp1[0] = newS1[0]
    dp2 = [0] * len(sequence)
    dp2[0] = newS2[0]
    
    for i in range(1,len(sequence)):
        dp1[i] = max(dp1[i - 1] + newS1[i], newS1[i])
        dp2[i] = max(dp2[i - 1] + newS2[i], newS2[i])
    
    return max(max(dp1),max(dp2))

print(solution([2,3,-6,1,3,-1,2,4]))