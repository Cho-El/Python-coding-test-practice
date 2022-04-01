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
    move = len(name) - 1
    for idx in range(len(name)):
        next_idx = idx + 1
        while (next_idx < len(name)) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, len(name) - next_idx)
        move = min(move, idx + len(name) - next_idx + distance)

    result += move
    return result

    # while True: # 왼쪽 오른쪽으로 이동
    #     cnt_index[now] = 0 # 해당 index를 확인하므로 0으로 초기화
    #     if sum(cnt_index) == 0: # 모든 합이 0이면 종료
    #         return result

    #     left, right = 1, 1
    #     while cnt_index[now - left] == 0: # 왼쪽으로 이동
    #         left += 1
    #     while cnt_index[now + right] == 0: # 오른쪽으로 이동
    #         right += 1
    #     if left < right:
    #         now -= left
    #         result += left
    #     else:
    #         now += right
    #         result += right
        
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

def solution2(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    print(answer, name)
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx) # 현재 위치에서
        move = min(move, idx + n - next_idx + distance)
        print(f'idx : {idx}, distance : {distance}, move : {move}')
   
    answer += move
    return answer

name = "JEROEN"
print(solution2(name))
