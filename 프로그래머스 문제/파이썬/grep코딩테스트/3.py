def solution(replies, n, k):
    answer = []

    for reply in replies:
        check = 0
        for cut in range(n, len(reply) // 2 + 1):
            for i in range(len(reply)):
                crit = reply[i:i + cut]
                next = reply[i + cut : i + 2 * cut]
                if crit == next: # 같다면 다음 것도 같은지 확인
                    cnt = 2
                    j = i + 2 * cut
                    while crit == next and cnt != k:
                        next = reply[j : j + cut]
                        if crit == next:
                            cnt += 1
                            j = j + cut
                    
                    if cnt == k: # 불량
                        answer.append(0)
                        check = 1
                        break

            if check == 1: # 불량인 경우
                break
        else:
            answer.append(1)

    return answer
if __name__ == '__main__':
    replies = [["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"]	,
            ["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"],
            ["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"],
            ["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"]]
    n = [3,2,4,3]
    k = [2,4,2,3]
    for replies, n, k in zip(replies, n, k):
        print(solution(replies, n, k))