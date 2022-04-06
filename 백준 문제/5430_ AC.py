# 구현, 자료구조, 문자열, 파싱, 덱
import sys
t = int(input())
for _ in range(t):
    dir = 1
    p = list(sys.stdin.readline().rstrip())
    n = int(input())
    temp = sys.stdin.readline().rstrip().strip('[]').split(',') # strip()사용
    if n != 0:
        array = list(map(int, temp))
    else:
        array = []

    for i in p:
        if i == 'R':
            dir *= -1
        else:
            if not array:
                print('error')
                break
            else:
                if dir == -1:
                    array.pop(-1)
                else:
                    array.pop(0)
    else:

        result = '[' + ','.join(map(str,array[::dir])) + ']' # join에 들어가는 리스트 값들은 무조건 string이어야한다.
        print(result)