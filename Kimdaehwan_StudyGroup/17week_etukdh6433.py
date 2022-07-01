"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
17주차 2206 벽 부수고 이동하기 (시간초과)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import math
import time

def find(arr):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dist = [[math.inf for i in range(c)] for j in range(r)]
    dist[0][0] = 1
    cnt = 0
    o = 0
    q = []
    q.append((0, 0))
    while q:
        t = q.pop(0)
        if dist[t[0]][t[1]] == math.inf:
            continue
        for k in range(4):
            nr = t[0] + dr[k]
            nc = t[1] + dc[k]
            if (nr >= 0) and (nr < r) and (nc >= 0) and (nc < c):
                if dist[nr][nc] > dist[t[0]][t[1]] + 1 and arr[nr][nc] == 0:
                    dist[nr][nc] = dist[t[0]][t[1]] + 1
                    q.append((nr, nc))
                elif dist[nr][nc] > dist[t[0]][t[1]] + 1 and cnt < 1:
                    dist[nr][nc] = dist[t[0]][t[1]] + 1
                    q.append((nr, nc))
                    o = 1
                elif dist[nr][nc] > dist[t[0]][t[1]] + 1 and cnt >= 1:
                    q.append((nr, nc))
        if o == 1:
            cnt += 1

    return dist


r, c = map(int, sys.stdin.readline().split())
nl = []
for i in range(r):
    nl.append(list(map(int, sys.stdin.readline().rstrip())))

dist = find(nl)

if dist[r-1][c-1] == math.inf:
    print(-1)
else:
    print(f"{dist[r-1][c-1]}")
