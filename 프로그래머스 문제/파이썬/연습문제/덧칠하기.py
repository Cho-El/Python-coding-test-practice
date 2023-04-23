def solution(n,m,section):
    start = 0
    result = 0
    while True:
        paintingLn = section[start] + m - 1
        result += 1
        while paintingLn >= section[start]:
            start += 1
            if len(section) == start:
                return result

print(solution(8,4,[2,3,6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))