def solution(balance, transaction, abnormal):
    new_balance = [[]]
    for idx, b in enumerate(balance):
        new_balance.append([[b,idx+1]])
    
    for t in transaction:
        user1, user2, money = t
        while money != 0:
            temp = new_balance[user1].pop() # 돈을 꺼냄
            if temp[0] > money:
                temp[0] -= money
                new_balance[user2].append([money, temp[1]])
                new_balance[user1].append([temp[0], temp[1]])
                money = 0

            else:
                money -= temp[0]
                new_balance[user2].append(temp)


    for a in abnormal:
        for i in range(1, len(new_balance)):
            for j in range(len(new_balance[i])):
                if a == new_balance[i][j][1]:
                    new_balance[i][j][0] = 0
    answer = []


    for i in range(1,len(new_balance)):
        sum = 0
        for v, idx in new_balance[i]:
            sum += v
        answer.append(sum)
    return answer

if __name__ == '__main__':
    balance = [[30, 30, 30, 30],[30, 30, 30, 30],[40, 30, 50],[100, 1, 1, 1, 1]]
    transaction = [[[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]],[[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]],[[1, 3, 20], [2, 1, 10], [3, 1, 45], [2, 3, 10], [1, 3, 35], [2, 1, 5], [3, 1, 10], [3, 2, 5]],[[1, 2, 100], [2, 3, 101], [3, 4, 102], [4, 5, 103], [5, 1, 104]]]
    abnormal = [[1],[2,3],[2],[1]]

    for b, t, a in zip(balance, transaction, abnormal):
        print(solution(b,t,a))
