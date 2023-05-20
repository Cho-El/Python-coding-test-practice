#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH centre
#  2. INTEGER_ARRAY status
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
from collections import deque
from collections import defaultdict
import sys
def findMinimumTime(centre_nodes, centre_from, centre_to, status):
    global answer
    answer = 0
    # Write your code here
    graph = defaultdict(list)
    for f, t in zip(centre_from,centre_to):
        graph[f].append(t)
        graph[t].append(f)
    
    visited = [0] * (centre_nodes + 1)
    startPoint = []
    targetPoint = []
    targetPointVisited = []
    
    for idx, s in enumerate(status, start = 1):
        if s == 1:
            targetPoint.append(idx)
        elif s == 3:
            startPoint.append(idx)
    
    bfs(graph, startPoint, visited, targetPoint, [])
    
    return answer
    
def bfs(graph, startPoint, visited, targetPoint, targetPointVisited):
    global answer
    q = deque(startPoint)
    while q:
        node = q.popleft()
        for nextNode in graph[node]:
            if not visited[nextNode] and nextNode not in startPoint:
                visited[nextNode] = visited[node] + 1
                q.append(nextNode)
                if nextNode in targetPoint:
                    answer = visited[nextNode]
                    targetPointVisited.append(0)
                    if len(targetPoint) == len(targetPointVisited):
                        return
    return
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    centre_nodes, centre_edges = map(int, input().rstrip().split())

    centre_from = [0] * centre_edges
    centre_to = [0] * centre_edges

    for i in range(centre_edges):
        centre_from[i], centre_to[i] = map(int, input().rstrip().split())

    status_count = int(input().strip())

    status = []

    for _ in range(status_count):
        status_item = int(input().strip())
        status.append(status_item)

    result = findMinimumTime(centre_nodes, centre_from, centre_to, status)

    fptr.write(str(result) + '\n')

    fptr.close()
