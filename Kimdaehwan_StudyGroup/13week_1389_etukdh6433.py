import sys
import math


def Floyd_Warshall(arr):
    dist = [[math.inf for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = arr[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n, m = map(int, sys.stdin.readline().split())
relation = [[math.inf for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    relation[a-1][a-1], relation[b-1][b-1] = 0, 0
    relation[a-1][b-1], relation[b-1][a-1] = 1, 1

dist = Floyd_Warshall(relation)

for i in range(n):
    if min(map(sum, dist)) == sum(dist[i]):
        print(f"{i+1}")
        break
