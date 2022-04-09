def insertV(dist, q, visited, i, op):
    for j in range(1, len(dist)):
        if j in visited:
            continue
        if dist[0][j] + dist[j][i] == dist[0][i]:
            q.append((op*dist[0][j], j))
            q.sort(key= lambda x: x[0])
            visited.add(j)

def solution(dist):
    answer = []
    q = [(0, 0)]
    visited = set([0])

    for i in range(len(dist)):
        if i in visited:
            continue

        if q[-1][0] > dist[0][i]:
            q.append((-dist[0][i], i))
            q.sort(key= lambda x: x[0])
            visited.add(i)

            insertV(dist, q, visited, i, -1)

        else:
            last = q[-1][1]
            if dist[0][last] + dist[last][i] == dist[0][i]:
                q.append((dist[0][i], i))
                q.sort(key= lambda x: x[0])
                visited.add(i)

                insertV(dist, q, visited, i, 1)
            else:
                q.append((-dist[0][i], i))
                q.sort(key= lambda x: x[0])
                visited.add(i)

                insertV(dist, q, visited, i, -1)

    result = [v for d, v in q]
    answer.append(result)
    answer.append(result[::-1])
    answer.sort(key=lambda x: x[0])

    return answer

dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
print(solution(dist))