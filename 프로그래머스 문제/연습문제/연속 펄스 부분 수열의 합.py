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
    
    start, end = 0, 0
    sum1 = 0
    sum2 = 0
    while start < len(sequence) and end < len(sequence):
        # 전까지의 최대합 보다 현재 까지의 합이 더 클 때
            # 현재 까지의 합으로 갱신 시켜준다.
            
        if sum1 < 
    return answer