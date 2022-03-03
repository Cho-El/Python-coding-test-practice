import heapq

def solution(operations):
    h = []
    answer = []
    for i in operations:
        letter, num = i.split()
        num = int(num)
        if letter == "I":
            heapq.heappush(h, num)

        elif letter == "D":
            try:
                if num == 1:
                    h = heapq.nlargest(len(h),h)[1:]
                    heapq.heapify(h)
                else:
                    heapq.heappop(h)
            except:
                continue
    
    if not h:
        return [0,0]
    else:
        max = heapq.nlargest(1,h)[0]
        min = h[0]
        return [max,min]

operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))