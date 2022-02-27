def distance(n,a,b):
    right = abs(a-b)
    left = abs(n+a-b)
    return min(right, left)

def solution(name):
    default = 'A' * len(name)
    result = 0 # 총 조작 횟수
    cnt_index = [0] * len(name) # 바뀐 문자의 인덱스들 저장
    # 쭉 돌면서 바꿔야 하는 문자 찾기
    for ix, (n,d) in enumerate(zip(name, default)):
        if n != d: # 바꿔줘야 하는 문자 찾음
            up = ord(n) - ord(d) # 위쪽으로 이동하는 거리
            down = ord('Z') - ord(n) + 1 # 아래쪽으로 이동하는 거리
            result += min(up, down)
            cnt_index[ix] = 1
    
    now = 0
    while True: # 왼쪽 오른쪽으로 이동
        cnt_index[now] = 0 # 해당 index를 확인하므로 0으로 초기화
        if sum(cnt_index) == 0: # 모든 합이 0이면 종료
            return result

        left, right = 1, 1
        while cnt_index[now - left] == 0: # 왼쪽으로 이동
            left += 1
        while cnt_index[now + right] == 0: # 오른쪽으로 이동
            right += 1
        if left < right:
            now -= left
            result += left
        else:
            now += right
            result += right
        
    # while cnt_index:
    #     next = (now+1) % len(cnt_index)
    #     prev = len(cnt_index)-1 if now - 1 < 0 else now - 1

    #     right = distance(len(name), cnt_index[now], cnt_index[next])
    #     left = distance(len(name),cnt_index[now], cnt_index[prev])
    #     cnt_index.remove(cnt_index[now])

    #     if left < right :
    #         now = prev - 1
    #         result += left
    #     else:
    #         now = next - 1
    #         result += right


name = "AAAB"
print(solution(name))

def solution(name):
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0

    while True:
        answer + change[idx]
        change[idx] = 0

