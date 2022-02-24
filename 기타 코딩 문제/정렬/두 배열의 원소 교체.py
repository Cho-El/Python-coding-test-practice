'''
동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서
두 원소를 서로 바꾸는 것을 말합니다.
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 합니다.
N,K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을
출력하는 프로그램을 작성하세요.

예를 들어 N = 5, K = 3
A = [1,2,5,4,3]
B = [5,5,6,6,5]

세 번의 연산 이후
A = [6,6,5,4,5]
B = [3,5,1,2,5]

ex)
5 3
1 2 5 4 3
5 5 6 6 5
출력 26
'''

n,k = map(int, input("숫자 두개를 입력하세요 : ").split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

def change(n,k):
    array1.sort()
    array2.sort(reverse = True)
    for i in range(k):
        if array1[i] < array2[i]:
            array1[i], array2[i] = array2[i], array1[i]
        else:
            break
    
    print(sum(array1))

change(n,k)


