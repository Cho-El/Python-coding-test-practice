# 선택 정렬
num = list(map(int, input("정렬할 숫자들을 입력해주세요 : ").split(' ')))
# # 재귀 함수
output = []
def select_sort1(num):
    # 종료조건
    if num == []:
        return []
    x = min(num)
    num.remove(min(num))
    return [x]+select_sort1(num)

print(select_sort1(num))

def select_sort2(num):
    l = len(num)
    start = 0
    while start < len(num)-1 :
        min_index = start
        for i in range(start, l):
            if num[min_index] > num[i]:
                min_index = i
        temp = num[min_index]
        num[min_index] = num[start]
        num[start] = temp
        start += 1
    return num
# print(select_sort2(num))