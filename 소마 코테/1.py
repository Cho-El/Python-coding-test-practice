import sys
sys.setrecursionlimit(10 ** 6)
def dfs(graph, visited, response, s):
    sum_res = 0
    total_cnt = 0
    non_res = []
    stack = [s]
    while stack:
        s = stack.pop()
        if not visited[s]:
            visited[s] = 1
            total_cnt += 1
            stack += graph[s]
            if response[s] != 0:
                sum_res += response[s]
            else:
                non_res.append(s)
    
    for nr in non_res:
        response[nr] = sum_res//(total_cnt - len(non_res))



def main():
    n,m,k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    response = [0] * (n+1)
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        response[a] = b
    
    for i in range(k):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        graph[a].sort(reverse = True)
        graph[b].sort(reverse = True)
    
    for i in range(1, n+1):
        if response[i] != 0 and not visited[i]:
            dfs(graph, visited, response, i)

    result = 0
    sum1 = 0
    cnt = 0
    for i in response[1:]:
        if i != 0:
            sum1 += i
            cnt += 1
    
    result = sum1/cnt        
    print(f'{result :.2f}')

if __name__=="__main__":
    main()

def main():
    n,m,k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    hate = []
    for i in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))
    
    for g in graph:
        for i in range(len(g)):
            if g[i] < 5:

    
    prefer.sort()
    
    

if __name__=="__main__":
    main()