'''
N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다. 다시 말해 앞쪽에
있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.
또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도 남아 있는 병사의 수가
최대가 되도록 하고 싶습니다.

1<=N<=2000

ex)
7
15 11 4 8 5 2 4
출력 2
'''
'''
아이디어 -> 부분 수열(LIS - 가장 긴 증가하는 부분 수열) 알고리즘 활용
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
모든 0<=j <i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
'''

n = int(input("입력해주세요 : "))
array = list(map(int,input().split()))

d = [1]*n
def soldier(n):
    for i in range(1,n):
        for j in range(0,i):
            if array[i] < array[j] :
                d[i] = max(d[i],d[j]+1)
    result = n - max(d)
    print(result)

soldier(n)