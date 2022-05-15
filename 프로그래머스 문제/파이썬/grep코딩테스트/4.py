def solution(n, rooks):
    graph = [[0 for _ in range(2 * n - 1)] for _ in range(n)]
    for i in range(n):
        start = (2 * n - 2 * i - 2) // 2
        for j in range(2 * i + 1):
            graph[i][start] = 1
            start += 1
    

if __name__ == '__main__':
    n = [3,5]
    rooks = [2,3]
    for n, rooks in zip(n, rooks):
        solution(n,rooks)