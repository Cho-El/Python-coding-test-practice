# 힙
import sys, heapq

# 1번 풀이
# def solution1(x):
#     if x == 0 :
#         if not q:
#             print(0)
#             return
#         else:
#             print(heapq.heappop(q)[1])
#             return
#     heapq.heappush(q,(abs(x),x))

# 2번 풀이
def solution2(x):
    if x == 0 :
        if not q1:
            if not q2:
                print(0)
                return
            else:
                print(-heapq.heappop(q2))
                return
        elif not q2:
            print(heapq.heappop(q1))
            return
        else:
            po = heapq.heappop(q1)
            ne = heapq.heappop(q2)

            if po >= ne:
                print(-ne)
                heapq.heappush(q1,po)
                return
            else:
                print(po)
                heapq.heappush(q2,ne)
            return

    if x > 0:
        heapq.heappush(q1,x) # 양수
    else:
        heapq.heappush(q2,-x) # 음수
if __name__ == '__main__':
    n = int(input())
    q = []
    q1 = []
    q2 = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        solution2(x)